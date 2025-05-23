from einops import reduce
import numpy as np
import torch
from torchvision import transforms
from tqdm import tqdm
from typing import Callable, Dict, List, Optional, Tuple

from xdiffusion.diffusion.ddpm import GaussianDiffusion_DDPM
from xdiffusion.diffusion import DiffusionModel
from xdiffusion.samplers.base import ReverseProcessSampler
from xdiffusion.utils import (
    load_yaml,
    DotConfig,
)


class GaussianDiffusionCascade(DiffusionModel):
    def __init__(self, config: DotConfig):
        super().__init__()
        self._config = config
        self._layers = torch.nn.ModuleList()

        layer_idx = 1
        while True:
            layer_name = f"cascade_layer_{layer_idx}"

            if not layer_name in config.diffusion_cascade:
                break

            config_path = config.diffusion_cascade[layer_name].config
            layer_config = load_yaml(config_path)
            self._layers.append(GaussianDiffusion_DDPM(layer_config))
            layer_idx += 1

    def print_model_summary(self):
        for layer in self._layers:
            layer.print_model_summary()

    def models(self) -> List[DiffusionModel]:
        models = []
        for m in self._layers:
            if isinstance(m, DiffusionModel):
                models.append(m)

        return models

    def config(self) -> DotConfig:
        return self._config

    def update_ema(
        self, step: int, total_steps: int, scale_fn: Callable[[int], Tuple[float, int]]
    ):
        # EMA not supported yet
        return

    def load_checkpoint(self, checkpoint_path: str):
        assert False, "Loading model weights for a cascade not supported yet."

    def configure_learning_rate_schedule(
        self, optimizers: List[torch.optim.Optimizer]
    ) -> List[torch.optim.lr_scheduler._LRScheduler]:
        schedules = []

        for layer, optimizer in zip(self._layers, optimizers):
            schedules.append(layer.configure_learning_rate_schedule([optimizer])[0])
        return schedules

    def configure_optimizers(self, learning_rate: float) -> List[torch.optim.Optimizer]:
        optimizers = []

        for layer in self._layers:
            optimizers.append(
                torch.optim.Adam(
                    layer.parameters(), lr=learning_rate, betas=(0.9, 0.99)
                )
            )
        return optimizers

    def forward(self, images: torch.FloatTensor, context: Dict, **kwargs):
        # Sum the losses from each of the stages
        stage_loss = 0
        for model in self.models():
            config_for_layer = model.config()
            context_for_layer = context.copy()
            images_for_layer = images

            if "super_resolution" in config_for_layer:
                # First create the low resolution context.
                low_resolution_spatial_size = (
                    config_for_layer.super_resolution.low_resolution_size
                )
                low_resolution_images = transforms.functional.resize(
                    images,
                    size=(
                        low_resolution_spatial_size,
                        low_resolution_spatial_size,
                    ),
                    antialias=True,
                )
                context_for_layer[
                    config_for_layer.super_resolution.conditioning_key
                ] = low_resolution_images

            # If the images are not the right shape for the model input, then
            # we need to resize them too. This could happen if we are the intermediate
            # super resolution layers of a multi-layer cascade.
            model_input_spatial_size = config_for_layer.data.image_size

            B, C, H, W = images.shape
            if H != model_input_spatial_size or W != model_input_spatial_size:
                images_for_layer = transforms.functional.resize(
                    images,
                    size=(
                        model_input_spatial_size,
                        model_input_spatial_size,
                    ),
                    antialias=True,
                )

            try:
                loss_dict = model.loss_on_batch(
                    images=images_for_layer, context=context_for_layer
                )
                loss = loss_dict["loss"]
            except torch.cuda.OutOfMemoryError as e:
                import gc

                for obj in gc.get_objects():
                    if torch.is_tensor(obj) and obj.is_cuda:
                        print(f"{type(obj)} : {obj.size()} {obj.shape} {obj.dtype}")
                raise e
            stage_loss += loss
        return {"loss": stage_loss}

    def loss_on_batch(self, images, context: Dict, stage_idx: int, **kwargs) -> Dict:
        """Calculates the reverse process loss on a batch of images.

        Args:
            image: Tensor batch of images, of shape [B, C, H, W]
            y: Class labels, if they exist.

        Returns:
            Dictionary of loss values, of which the "loss" entry will
            be the training loss.
        """
        raise NotImplementedError("Cascade loss is calculated at individual stages.")

    def sample(
        self,
        context: Optional[Dict] = None,
        num_samples: int = 16,
        guidance_fn: Optional[Callable] = None,
        classifier_free_guidance: Optional[float] = None,
        sampler: Optional[ReverseProcessSampler] = None,
        initial_noise: Optional[torch.Tensor] = None,
        context_preprocessor: Optional[torch.nn.Module] = None,
    ) -> Tuple[torch.Tensor, Optional[List[torch.Tensor]]]:
        assert initial_noise is None
        assert sampler is None

        # Sample from each stage, passing the results to each next stage.
        all_stage_output = []
        output_from_previous_layer = None
        for diffusion_model in self.models():
            context_for_layer = context.copy() if context is not None else {}

            if output_from_previous_layer is not None:
                context_for_layer[
                    diffusion_model.config().super_resolution.conditioning_key
                ] = output_from_previous_layer

            output_from_previous_layer, _ = diffusion_model.sample(
                context=context_for_layer,
                num_samples=num_samples,
                guidance_fn=guidance_fn,
                classifier_free_guidance=classifier_free_guidance,
            )
            all_stage_output.append(output_from_previous_layer)
        return output_from_previous_layer, all_stage_output

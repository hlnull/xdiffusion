# xdiffusion
A unified media (Image, Video, Audio, Text) diffusion repository, for education and learning.

If you are looking for just the lessons on image diffusion models, checkout [mindiffusion](https://github.com/swookey-thinky/mindiffusion) for more image diffusion model paper implementations.

## Requirements

This package built using PyTorch and written in Python 3. Due to package dependencies, this repo requires python 3.10 or greater. To setup an environment to run all of the lessons, we suggest using conda or venv:

```
> python3 -m venv xdiffusion_env
> source xdiffusion_env/bin/activate
> pip install --upgrade pip
> pip install -r requirements.txt
```
I find [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv) to be very helpful as well, in managing both the virtual environment as well as the python version dependencies.

```
> pyenv install 3.10.15
> pyenv virtualenv 3.10.15 xdiffusion_env
> pyvenv activate xdiffusion_env     
> pip install --upgrade pip
> pip install -r requirements.txt
```

All lessons are designed to be run from the root of the repository, and you should set your python path to include the repository root:

```
> export PYTHONPATH=$(pwd)
```

If you have issues with PyTorch and different CUDA versions on your instance, make sure to install the correct version of PyTorch for the CUDA version on your machine. For example, if you have CUDA 11.8 installed, you can install PyTorch using:

```
> pip install torch==2.1.0 torchvision --index-url https://download.pytorch.org/whl/cu118
```

## Image Diffusion

### Training Datasets

In this repository, we will be working with the [MNIST](https://en.wikipedia.org/wiki/MNIST_database) dataset because it is simple and can be trained in real time with minimal GPU power and memory. The main difference between MNIST and other datasets is the single channel of the imagery, versus 3 channels in most other datasets. We will make sure that the models we build can easily accomodate 1- or 3-channel data, so that you can test the models we build on other datasets.

### Image Models
The following is a list of the supported image models, their current results, and a link to their configuration files and documentation.

| Date  | Name  | Paper | Config | Results | Instructions
| :---- | :---- | ----- | ------ | ----- | -----
| June 2020 | DDPM | [Denoising Diffusion Probabilistic Models](https://arxiv.org/abs/2006.11239) | [config](https://github.com/swookey-thinky/xdiffusion/blob/main/configs/image/mnist/ddpm_32x32_epsilon_discrete.yaml) | ![DDPM](https://drive.google.com/uc?export=view&id=1Yd8hhK9EhFMhfqQJf3CjAtFqK_XdZPSi)| [instructions](https://github.com/swookey-thinky/xdiffusion/blob/main/docs/image/ddpm.md)
| November 2020 | Score-SDE | [Score-Based Generative Modeling through Stochastic Differential Equations](https://arxiv.org/abs/2011.13456) | [config](https://github.com/swookey-thinky/xdiffusion/blob/main/configs/image/mnist/score_sde_subvpsde.yaml) | ![Sub-VPE SDE](https://drive.google.com/uc?export=view&id=1SPCFu0aFkcfXKpmLE2p3RteIZ-dCBeuA)| [instructions](https://github.com/swookey-thinky/xdiffusion/blob/main/docs/image/score_sde.md)
| July 2021 | D3PM | [Structured Denoising Diffusion Models in Discrete State-Spaces](https://arxiv.org/abs/2107.03006) | | | 
| May 2022 | Imagen | [Photorealistic Text-to-Image Diffusion Models with Deep Language Understanding](https://arxiv.org/abs/2205.11487) | [config](https://github.com/swookey-thinky/xdiffusion/blob/main/configs/image/mnist/imagen.yaml) |  ![Imagen](https://drive.google.com/uc?export=view&id=1MKyRgPKoPRFHLzd78aTA1K3QHgNm08Px) | [instructions](https://github.com/swookey-thinky/xdiffusion/blob/main/docs/image/imagen.md)
| June 2022 | EDM | [Elucidating the Design Space of Diffusion-Based Generative Models](https://arxiv.org/abs/2206.00364) | [config](https://github.com/swookey-thinky/xdiffusion/blob/main/configs/image/mnist/edm.yaml) |  ![EDM](https://drive.google.com/uc?export=view&id=1yUeR5ep9mK1IwMsTyHwhyAqlftFwBNYz) | [instructions](https://github.com/swookey-thinky/xdiffusion/blob/main/docs/image/edm.md)
| September 2022 | Rectified Flow | [Flow Straight and Fast: Learning to Generate and Transfer Data with Rectified Flow](https://arxiv.org/abs/2209.03003) | [config](https://github.com/swookey-thinky/xdiffusion/blob/main/configs/image/mnist/rectified_flow_32x32.yaml) |  ![Rectified Flow](https://drive.google.com/uc?export=view&id=14TOqFXSWiFpeUVnDuMfLRcRDUV5onuKQ) | [instructions](https://github.com/swookey-thinky/xdiffusion/blob/main/docs/image/rectified_flow.md)
| December 2022 | LoRA | [LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685) | - | ![LoRA](https://drive.google.com/uc?export=view&id=1NGtmYiLNAtOTC46UK7nbpkGf3NYfSVWI) | [instructions](https://github.com/swookey-thinky/xdiffusion/blob/main/docs/image/lora.md)
| December 2022 | DiT | [Scalable Diffusion Models with Transformers](https://arxiv.org/abs/2212.09748) | [config](https://github.com/swookey-thinky/xdiffusion/blob/main/configs/image/mnist/dit.yaml) |  ![DiT](https://drive.google.com/uc?export=view&id=1J6ktzFr7iqgWcf23JpgVaM81Z7sUUcmj) | [instructions](https://github.com/swookey-thinky/xdiffusion/blob/main/docs/image/dit.md)
| March 2023 | Consistency Models | [Consistency Models](https://arxiv.org/abs/2303.01469) | [config](https://github.com/swookey-thinky/xdiffusion/blob/main/configs/image/mnist/consistency_model.yaml) |  ![Consistency Model](https://drive.google.com/uc?export=view&id=1Zgj38dDdEwGvHKFMJ0zgR37zrA5fQ-vx) | [instructions](https://github.com/swookey-thinky/xdiffusion/blob/main/docs/image/consistency_model.md)
| September 2023 | PixArt-α | [PixArt-α: Fast Training of Diffusion Transformer for Photorealistic Text-to-Image Synthesis](https://arxiv.org/abs/2310.00426) | [config](https://github.com/swookey-thinky/xdiffusion/blob/main/configs/image/mnist/pixart_alpha.yaml) | ![Pixart-Alpha](https://drive.google.com/uc?export=view&id=17hrD-Zxreb7XNpETWE4MdfVeqs1fnQXu) | [instructions](https://github.com/swookey-thinky/xdiffusion/blob/main/docs/image/pixart_alpha.md)
| November 2023 | DiffuSSM | [Diffusion Models Without Attention]() | [config](https://github.com/swookey-thinky/xdiffusion/blob/main/configs/image/mnist/diffussm.yaml) | ![DiffuSSM](https://drive.google.com/uc?export=view&id=1YKO1JUGeW9DbzqtGtA3HAz_gcNLKnBlZ) | [instructions](https://github.com/swookey-thinky/xdiffusion/blob/main/docs/image/diffussm.md)
| March 2024 | Stable Diffusion 3 | [Scaling Rectified Flow Transformers for High-Resolution Image Synthesis](https://arxiv.org/abs/2403.03206) | [config](https://github.com/swookey-thinky/xdiffusion/blob/main/configs/image/mnist/sd3.yaml) | ![SD3](https://drive.google.com/uc?export=view&id=1YI6iezQHbyAKiyyChnyD6_8KQaPdxIxn) | [instructions](https://github.com/swookey-thinky/xdiffusion/blob/main/docs/image/sd3.md)
| July 2024 | AuraFlow | [Introducing AuraFlow v0.1, an Open Exploration of Large Rectified Flow Models](https://blog.fal.ai/auraflow/) | [config](https://github.com/swookey-thinky/xdiffusion/blob/main/configs/image/mnist/auraflow.yaml) | ![AuraFlow](https://drive.google.com/uc?export=view&id=1_qODQDHpEZrverYHqa6_uH0QnLy7Tf4f) | [instructions](https://github.com/swookey-thinky/xdiffusion/blob/main/docs/image/auraflow.md)
| August 2024 | Flux | [Flux Announcement](https://blackforestlabs.ai/announcing-black-forest-labs/) | [config](https://github.com/swookey-thinky/xdiffusion/blob/main/configs/image/mnist/flux.yaml) | ![Flux](https://drive.google.com/uc?export=view&id=1_r8poe1SJxf8UtT4mmQaTT378m26hD-F) | [instructions](https://github.com/swookey-thinky/xdiffusion/blob/main/docs/image/flux.md)
| October 2024 | Sana | [SANA: Efficient High-Resolution Image Synthesis with Linear Diffusion Transformers](https://arxiv.org/abs/2410.10629) | [config](https://github.com/swookey-thinky/xdiffusion/blob/main/configs/image/mnist/sana.yaml) | ![Sana](https://drive.google.com/uc?export=view&id=1_sUwEAQkN58xtGwJP69q94WO9NxmOWDO) | [instructions](https://github.com/swookey-thinky/xdiffusion/blob/main/docs/image/sana.md)
| October 2024 | Stable Diffusion 3.5 | [Introducing Stable Diffusion 3.5](https://stability.ai/news/introducing-stable-diffusion-3-5) | [config](https://github.com/swookey-thinky/xdiffusion/blob/main/configs/image/mnist/sd3.5.yaml) | ![SD 3.5](https://drive.google.com/uc?export=view&id=1_6GKNeTazoZ2RqEyxN2ta8B9UAdBPffB) | [instructions](https://github.com/swookey-thinky/xdiffusion/blob/main/docs/image/sd35.md)
| November 2024 | | [Training-free Regional Prompting for Diffusion Transformers](https://arxiv.org/abs/2411.02395) | | |
| November 2024 | JanusFlow | [JanusFlow: Harmonizing Autoregression and Rectified Flow for Unified Multimodal Understanding and Generation](https://arxiv.org/abs/2411.07975) | | |

## Video Diffusion

### Training Datasets

Due to the resource constraints of most models, we have decided to use the [Moving MNIST](https://www.cs.toronto.edu/~nitish/unsupervised_video/) dataset to train on. Moving MNIST is a simple dataset similar to MNIST, of digits which move around the screen. It is an unlabeled dataset, so we do not have access to text labels to determine which digits are moving around the screen, but we will address that deficiency as well. We train at a reduced resolution of `32x32`, due to the resource constraints that most models require. This allows us to train most diffusion models on a T4 instance, which is free to run on [Google Colab](https://colab.research.google.com/). We limit training and sample generation to 16 frames, even though the source dataset contains 20 frames.

Sample from the original dataset:

![Moving MNIST](https://drive.google.com/uc?export=view&id=1FS9lEd6DPFJ4Ka7hUgqk2BlsJ8FzOdPE)

### Video Diffusion Models
The following is a list of the supported video models, their current results, and a link to their configuration files and documentation.

| Date  | Name  | Paper | Config | Results | Instructions
| :---- | :---- | ----- | ------ | ----- | -----
| April 2022 | Video Diffusion Models | [Video Diffusion Models](https://arxiv.org/abs/2204.03458) | [config](https://github.com/swookey-thinky/xdiffusion/blob/main/configs/video/moving_mnist/video_diffusion_models.yaml) | ![Video Diffusion Models](https://drive.google.com/uc?export=view&id=1pF6WVY8_dlGudxZIsml3VWPxbUs0ONfa) | [instructions](https://github.com/swookey-thinky/xdiffusion/blob/main/docs/video/video_diffusion_models.md)
| May 2022 | CogVideo | [CogVideo: Large-scale Pretraining for Text-to-Video Generation via Transformers](https://arxiv.org/abs/2205.15868) | | |
| May 2022 | FDM | [Flexible Diffusion Modeling of Long Videos](https://arxiv.org/abs/2205.11495) | [config](https://github.com/swookey-thinky/xdiffusion/blob/main/configs/video/moving_mnist/flexible_diffusion_modeling.yaml) | ![Flexible Diffusion Models](https://drive.google.com/uc?export=view&id=1B2raR3_suRf8qAUP4jzi8YIwka-UHwrU) | [instructions](https://github.com/swookey-thinky/xdiffusion/blob/main/docs/video/flexible_diffusion_modeling.md)
| September 2022 | Make-A-Video | [Make-A-Video: Text-to-Video Generation without Text-Video Data](https://arxiv.org/abs/2209.14792) | [config](https://github.com/swookey-thinky/xdiffusion/blob/main/configs/video/moving_mnist/make_a_video.yaml) |  ![Make-A-Video](https://drive.google.com/uc?export=view&id=1dm4H7lsliib4KW-4T4DJeiFLRi2Ph2JD) | [instructions](https://github.com/swookey-thinky/xdiffusion/blob/main/docs/video/make_a_video.md)
| October 2022 | Imagen Video | [Imagen Video: High Definition Video Generation with Diffusion Models](https://arxiv.org/abs/2210.02303) | [config](https://github.com/swookey-thinky/xdiffusion/blob/main/configs/video/moving_mnist/imagen_video.yaml) |  ![Imagen Video](https://drive.google.com/uc?export=view&id=1TKwiYQYnIZZ8fM5juQMEeJkc6clPkCvV) | [instructions](https://github.com/swookey-thinky/xdiffusion/blob/main/docs/video/imagen_video.md)
| October 2022 | Phenaki | [Phenaki: Variable Length Video Generation From Open Domain Textual Description](https://arxiv.org/abs/2210.02399) | | |
| December 2022 | Tune-A-Video  | [Tune-A-Video: One-Shot Tuning of Image Diffusion Models for Text-to-Video Generation](https://arxiv.org/abs/2212.11565) | | |
| February 2023 | Gen-1 | [Structure and Content-Guided Video Synthesis with Diffusion Models](https://arxiv.org/abs/2302.03011) | | |
| March 2023 | Text2Video-Zero | [Text2Video-Zero: Text-to-Image Diffusion Models are Zero-Shot Video Generators](https://arxiv.org/abs/2303.13439) | | |
| April 2023 | Video LDM | [Align your Latents: High-Resolution Video Synthesis with Latent Diffusion Models](https://arxiv.org/abs/2304.08818) | [config](https://github.com/swookey-thinky/xdiffusion/blob/main/configs/video/moving_mnist/video_ldm.yaml) | ![Video LDM](https://drive.google.com/uc?export=view&id=1UsKoMKyaeQspVGxNhhowWx7OQ57XEIiH) | [instructions](https://github.com/swookey-thinky/xdiffusion/blob/main/docs/video/video_ldm.md)
| May 2023 | Control-Video | [ControlVideo: Training-free Controllable Text-to-Video Generation](https://arxiv.org/abs/2305.13077) | | |
| May 2023 | PYoCo | [Preserve Your Own Correlation: A Noise Prior for Video Diffusion Models](https://arxiv.org/abs/2305.10474) | | |
| July 2023 | AnimateDiff | [AnimateDiff: Animate Your Personalized Text-to-Image Diffusion Models without Specific Tuning](https://arxiv.org/abs/2307.04725) | [config](https://github.com/swookey-thinky/xdiffusion/blob/main/configs/video/moving_mnist/animate_diff.yaml) | ![Animate Diff](https://drive.google.com/uc?export=view&id=11EJWvEilKqmrGabCRvjM5CxW6I7mWEEg) | [instructions](https://github.com/swookey-thinky/xdiffusion/blob/main/docs/video/animate_diff.md) 
| August 2023 | ModelScopeT2V | [ModelScope Text-to-Video Technical Report](https://arxiv.org/abs/2308.06571) | | |
| September 2023 | Show-1 | [Show-1: Marrying Pixel and Latent Diffusion Models for Text-to-Video Generation](https://arxiv.org/abs/2309.15818) | | |
| September 2023 | LaVie | [LAVIE: High-Quality Video Generation with Cascaded Latent Diffusion Models](https://arxiv.org/abs/2309.15103) | | |
| October 2023 | VideoCrafter 1 | [VideoCrafter1: Open Diffusion Models for High-Quality Video Generation](https://arxiv.org/abs/2310.19512) | | |
| November 2023 | Emu Video | [Emu Video: Factorizing Text-to-Video Generation by Explicit Image Conditioning](https://arxiv.org/abs/2311.10709) | | |
| November 2023 | | [Decouple Content and Motion for Conditional Image-to-Video Generation](https://arxiv.org/abs/2311.14294) | | |
| November 2023 | Stable Video Diffusion | [Stable Video Diffusion: Scaling Latent Video Diffusion Models to Large Datasets](https://arxiv.org/abs/2311.15127) | | |
| December 2023 | VideoBooth | [VideoBooth: Diffusion-based Video Generation with Image Prompts](https://arxiv.org/abs/2312.00777) | | |
| December 2023 | LivePhoto | [LivePhoto: Real Image Animation with Text-guided Motion Control](https://arxiv.org/abs/2312.02928) | | |
| December 2023 | HiGen | [Hierarchical Spatio-temporal Decoupling for Text-to-Video Generation](https://arxiv.org/abs/2312.04483) | | |
| December 2023 | AnimateZero | [AnimateZero: Video Diffusion Models are Zero-Shot Image Animators](https://arxiv.org/abs/2312.03793) | | |
| December 2023 | W.A.L.T | [Photorealistic Video Generation with Diffusion Models](https://arxiv.org/abs/2312.06662) | | |
| December 2023 | VideoLCM | [VideoLCM: Video Latent Consistency Model](https://arxiv.org/abs/2312.09109) | | |
| December 2023 | GenTron | [GenTron: Diffusion Transformers for Image and Video Generation](https://arxiv.org/abs/2312.04557) | | |
| January 2024 | Latte | [Latte: Latent Diffusion Transformer for Video Generation](https://arxiv.org/abs/2401.03048) | | |
| January 2024 | VideoCrafter 2 | [VideoCrafter2: Overcoming Data Limitations for High-Quality Video Diffusion Models](https://arxiv.org/abs/2401.09047) | | |
| January 2024 | Lumiere | [Lumiere: A Space-Time Diffusion Model for Video Generation](https://arxiv.org/abs/2401.12945) | | |
| February 2024 | AnimateLCM | [AnimateLCM: Accelerating the Animation of Personalized Diffusion Models and Adapters with Decoupled Consistency Learning](https://arxiv.org/abs/2402.00769) | | |
| February 2024 | Video-LaVIT | [Video-LaVIT: Unified Video-Language Pre-training with Decoupled Visual-Motional Tokenization](https://arxiv.org/abs/2402.03161) | | |
| February 2024 | Snap Video | [Snap Video: Scaled Spatiotemporal Transformers for Text-to-Video Synthesis](https://arxiv.org/abs/2402.14797) | | |
| February 2024 | SORA | [Video generation models as world simulators](https://openai.com/index/video-generation-models-as-world-simulators/) [alternative](https://arxiv.org/abs/2402.17177) | [config](https://github.com/swookey-thinky/xdiffusion/blob/main/configs/video/moving_mnist/sora.yaml) |  ![SORA](https://drive.google.com/uc?export=view&id=1W40uY3xU5F36YTou-RT26Q6YidmrcJsp) | [instructions](https://github.com/swookey-thinky/xdiffusion/blob/main/docs/video/sora.md)
| April 2024 | TI2V-Zero | [TI2V-Zero: Zero-Shot Image Conditioning for Text-to-Video Diffusion Models](https://arxiv.org/abs/2404.16306) | | |
| May 2024 | Vidu | [Vidu: a Highly Consistent, Dynamic and Skilled Text-to-Video Generator with Diffusion Models](https://arxiv.org/abs/2405.04233) | | |
| May 2024 | FIFO-Diffusion | [FIFO-Diffusion: Generating Infinite Videos from Text without Training](https://arxiv.org/abs/2405.11473) | | |
| May 2024 | MOFA-VIdeo | [MOFA-Video: Controllable Image Animation via Generative Motion Field Adaptions in Frozen Image-to-Video Diffusion Model](https://arxiv.org/abs/2405.20222) | | |
| May 2024 | T2V-Turbo | [T2V-Turbo: Breaking the Quality Bottleneck of Video Consistency Model with Mixed Reward Feedback](https://arxiv.org/abs/2405.18750) | | |
| July 2024 | Diffusion Forcing | [Diffusion Forcing: Next-token Prediction Meets Full-Sequence Diffusion](https://arxiv.org/abs/2407.01392) | | |
| August 2024 | GameNGen | [Diffusion Models Are Real-Time Game Engines](https://arxiv.org/abs/2408.14837) | | |
| August 2024 | CogVideoX | [CogVideoX: Text-to-Video Diffusion Models with An Expert Transformer](https://arxiv.org/abs/2408.06072) | | |
| October 2024 | Movie-Gen | [Movie Gen: A Cast of Media Foundation Models](https://ai.meta.com/static-resource/movie-gen-research-paper) | | |
| October 2024 | Pyramid Flow | [Pyramidal Flow Matching for Efficient Video Generative Modeling](https://arxiv.org/abs/2410.05954) | | |
| October 2024 | T2V-Turbo-v2 | [T2V-Turbo-v2: Enhancing Video Generation Model Post-Training through Data, Reward, and Conditional Guidance Design](https://arxiv.org/abs/2410.05677) | | |
| December 2024 | LTX Video | [LTX-Video: Realtime Video Latent Diffusion](https://arxiv.org/abs/2501.00103)| [config](https://github.com/swookey-thinky/xdiffusion/blob/main/configs/video/moving_mnist/ltx_video/ltx_video.yaml)  | ![LTX Video](https://drive.google.com/uc?export=view&id=1zOCNPirEWQkL_REV6pNFdakkBVcnDBrB) | [instructions](https://github.com/swookey-thinky/xdiffusion/blob/main/docs/video/ltx_video.md)

## Audio Diffusion

### Audio Diffusion Models
The following is a list of the supported audio diffusion models, their current results, and a link to their configuration files and documentation.

| Date  | Name  | Paper | Config | Results | Instructions
| :---- | :---- | ----- | ------ | ----- | -----
| February 2022 | SaShiMi| [It's Raw! Audio Generation with State-Space Models](https://arxiv.org/abs/2202.09729) | | |
| January 2023 | Make-An-Audio | [Make-An-Audio: Text-To-Audio Generation with Prompt-Enhanced Diffusion Models](https://arxiv.org/abs/2301.12661) | [config](https://github.com/swookey-thinky/xdiffusion/blob/main/configs/audio/urbansound8k/make_an_audio.yaml) | | [instructions](https://github.com/swookey-thinky/xdiffusion/blob/main/docs/audio/make_an_audio.md)
| January 2023 | AudioLDM | [AudioLDM: Text-to-Audio Generation with Latent Diffusion Models](https://arxiv.org/abs/2301.12503) | | |
| June 2023 | VoiceBox | [Voicebox: Text-Guided Multilingual Universal Speech Generation at Scale](https://arxiv.org/abs/2306.15687) | | |
| August 2023 | AudioLDM 2 | [AudioLDM 2: Learning Holistic Audio Generation with Self-supervised Pretraining](https://arxiv.org/abs/2308.05734) | | |
| August 2023 | MusicLDM | [MusicLDM: Enhancing Novelty in Text-to-Music Generation Using Beat-Synchronous Mixup Strategies](https://arxiv.org/abs/2308.01546) | | |
| December 2023 | AudioBox | [Audiobox: Unified Audio Generation with Natural Language Prompts](https://arxiv.org/abs/2312.15821) | | |
| July 2024 | Stable Audio Open | [Stable Audio Open](https://arxiv.org/abs/2407.14358) | | | 

## TODO

- [x] Port the image diffusion repository
- [x] Port the video diffusion respository
- [ ] Unify all of the different attention mechanisms under Transformer based (B, L, D) and pixel based (B, C, H, W).

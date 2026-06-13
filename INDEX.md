# ComfyUI 工作流索引

> 自动生成 · 按内容分类 · 共 583 个工作流 · 更新于 2026-06-22

---


## 🎬 AI动画视频（117 个）

| 工作流文件 | 作用描述 | 主要模型 |
|-----------|---------|---------|
| 25秒的生命 | AnimateDiff 长序列叙事动画 | `dreamshaper_8` _(+1)_ |
| AbstractNoodleSoup | AnimateDiff 动画生成、＋超分放大 | `nooshpere_4.7` · `add_detail` (LoRA) · `4x-UltraSharp` (Up) _(+3)_ |
| AnimateDiff-ControlNet动画工作流 | AnimateDiff 视频风格转绘、ControlNet 姿态控制生成 | `ink_splashing` (LoRA) · `control_v11p_sd15_openpose` (CN) _(+1)_ |
| AnimateDiff-IPAdapter_控制网络 | AnimateDiff 视频风格转绘、IPAdapter+ 增强风格参考 | `revAnimated_v122` · `thickline_fp16` (LoRA) · `ip-adapter-plus_sd15` (IPA) _(+5)_ |
| AnimateDiff_ControlNet_Openpose_Depth | AnimateDiff 动画生成、ControlNet 姿态控制生成 | `control_v11f1p_sd15_depth_fp16` (CN) _(+2)_ |
| AnimateDiff_ControlNet动画_v2_-_LCM | AnimateDiff 动画生成、ControlNet 姿态控制生成 | `lcm_pytorch_lora_weights` (LoRA) · `control_v11p_sd15_openpose` (CN) _(+2)_ |
| AnimateDiff_动画生成修复 | AnimateDiff 动画生成、ControlNet 姿态控制生成 | `imp_v10` · `lcm_pytorch_lora_weights` (LoRA) · `control_v11p_sd15_openpose` (CN) _(+2)_ |
| AnimateDiff_控制网络-LCM | AnimateDiff 动画生成、ControlNet 姿态控制生成 | `lcm_pytorch_lora_weights` (LoRA) · `control_v11p_sd15_openpose` (CN) _(+2)_ |
| AnimateDiff_无闪烁动画视频工作流 | AnimateDiff 视频风格转绘、ReActor 视频换脸、IPAdapter FaceID 人脸一致性生成 | `lcm-lora-sdv1-5_lora_weights` (LoRA) · `ip-adapter-faceid-plusv2_sd15` (IPA) · `control_v11f1p_sd15_depth` (CN) _(+9)_ |
| AnimateDiff动画控制网络 | AnimateDiff 动画生成、ControlNet 姿态控制生成 | `control_v11p_sd15_openpose` (CN) _(+2)_ |
| AnimateDiff动画长度控制 | AnimateDiff 动画生成、ControlNet 线稿引导生成 | `3dAnimationDiffusion_v10` · `control_v11p_sd15_lineart` (CN) _(+1)_ |
| AnimateDiff带文本框工作流 | AnimateDiff 动画生成 | `revAnimated_v122EOL` |
| AnimateDiff文本描述动画 | AnimateDiff 动画生成 | `金色幻想1.5` _(+1)_ |
| AnimateDiff文生视频图生视频 | AnimateDiff 文字驱动视频 | — |
| Animatediff-LCM | AnimateDiff 视频风格转绘、ControlNet 姿态控制生成 | `LCM_LoRA_Weights_SD15` (LoRA) · `control_v11p_sd15_lineart_fp16` (CN) _(+2)_ |
| FreeU图像优化工作流 | SVD 图像转视频 | `svd_xt` |
| IPAdapter_AnimateDiff | AnimateDiff 动画生成、IPAdapter+ 增强风格参考、＋面部细节增强 | `XXMix_9realistic_v4.0_v4.0` · `lcm-lora-sdv1-5` (LoRA) · `ip-adapter-plus_sd15` (IPA) _(+10)_ |
| Image_Gif_Workflow | SVD 图像转视频、＋超分放大 | `airtistAnimated_v10` · `4x-UltraSharp` (Up) _(+1)_ |
| QRCode_Ipadapter生成可控丝滑动画 | AnimateDiff 视频风格转绘、ControlNet QR码特效 | `juggernaut_reborn` · `AnimateLCM_sd15_t2v_lora` (LoRA) · `VIT-G (medium strength)` (IPA) _(+2)_ |
| QRCode_IpdapterV2.0_AnimateLCM生成可控动画 | AnimateDiff 视频风格转绘、ControlNet QR码特效 | `majicMIX realistic(v7)` · `VIT-G (medium strength)` (IPA) · `control_v1p_sd15_qrcode_monster_v2` (CN) _(+2)_ |
| SDXL_-_SVD_-_25帧 | SVD XT 长视频生成 | `Video-svd_xt` · `LCM_SDXL_pytorch_lora_weights` (LoRA) _(+1)_ |
| SVD_-_AnimateDiff_Refiner_Upscaler | SVD 图像转视频、AnimateDiff 动画生成、＋超分放大 | `aniverse_v15Pruned` · `lcm_pytorch_lora_weights` (LoRA) · `control_v11p_sd15_softedge` (CN) _(+2)_ |
| SVD_XT工作流 | SVD XT 长视频生成 | `svd_xt` |
| SVD_文生图_图生视频基本工作流 | SVD 图像转视频 | `juggernautXL_version5` _(+1)_ |
| SVD图生视频-基础版 | SVD 图生视频（基础教程） | `svd_xt_1_1` |
| SVD放大和人脸修复_适用于中等广角镜头 | SVD 图像转视频、AnimateDiff 动画生成、＋超分放大 | `svd_xt-fp16` · `epoch885_OmniSR` (Up) · `GFPGANv1.4` (FR) _(+3)_ |
| SVD生成视频 | SVD 图像转视频 | `svd_xt_1_1` |
| SparseCtrl_model和AnimateDiff动画 | AnimateDiff SparseCtrl 稀疏运动控制 | `GhostMix(v2.0-BakedVAE)` · `LCM-LoRA for基础模型1.5(v1.0)` (LoRA) _(+2)_ |
| Text_Animation_with | AnimateDiff 视频风格转绘、ControlNet QR码特效、＋超分放大 | `v3_sd15_adapter` (LoRA) · `control_v1p_sd15_qrcode_monster` (CN) · `4x-UltraSharp` (Up) _(+1)_ |
| VTV加强 | AnimateDiff 视频风格转绘、IPAdapter+ 增强风格参考 | `ip-adapter-plus_sd15` (IPA) · `control_v11e_sd15_ip2p_fp16` (CN) _(+7)_ |
| Vid2Vid视频转绘 | AnimateDiff 视频风格转绘、ControlNet 深度图引导生成 | `counterfeitxl_v10` · `t2i-adapter_diffusers_xl_depth_…` (CN) _(+1)_ |
| Zero123_Animatediff_V3 | AnimateDiff 动画生成、Zero123 多角度三维视图、IPAdapter FaceID 人脸一致性生成 | `realisticVisionV51_v51VAE` · `ip-adapter-faceid_sd15_lora` (LoRA) · `ip-adapter-faceid_sd15` (IPA) _(+10)_ |
| animatediff | AnimateDiff 视频风格转绘、ControlNet Tile 高清重绘 | `control_v11f1e_sd15_tile_fp16` (CN) _(+3)_ |
| animatediff动画工作流 | AnimateDiff 动画生成 | `南柯一梦丨YUEMIX(V1.0)` _(+1)_ |
| animatediff视频转绘工作流 | AnimateDiff 视频风格转绘、ControlNet Tile 高清重绘 | `control_v11f1e_sd15_tile_fp16` (CN) _(+3)_ |
| get_image_size_workflow_如果报红需要下插件 | SVD 图生视频（基础教程） | `svd_xt` |
| openpose控制网络模板 | AnimateDiff 视频风格转绘、ControlNet 姿态控制生成 | `dreamshaper_8` · `v3_sd15_adapter` (LoRA) · `motion` (CN) _(+2)_ |
| svd_workflow | SVD 图生视频（基础教程） | `svd_xt` |
| workflow_txt_to_img_to_video | SVD XT 长视频生成 | `sd_xl_1.0` _(+1)_ |
| 一笔舞动 | SVD 图像转视频 | `svd_xt` _(+1)_ |
| 一键图生视频 | SVD 图像转视频 | `svd_xt` |
| 丝滑动画 | AnimateDiff 丝滑流畅动画 | `真实系：majicmixRealistic_v7` · `latent-consistencylcm-lora-sdv1-5` (LoRA) _(+2)_ |
| 丝滑无闪烁视频转绘 | AnimateDiff 视频风格转绘、ControlNet 姿态控制生成、＋超分放大 | `墨幽︱二次元(v2)` · `LCM-LoRA for基础模型1.5(v1.0)` (LoRA) · `control_v11f1p_sd15_depth` (CN) _(+5)_ |
| 任何人都可以跳舞_-_MagicAnimate | AnimateDiff 视频风格转绘、MagicAnimate 姿态驱动动画、ReActor 视频换脸 | `diffusion_pytorch_model` · `ip-adapter-plus_sd15` (IPA) · `control_v11p_sd15_lineart_fp16` (CN) _(+3)_ |
| 使用IPadapter和controlnets的Animatediff | AnimateDiff 视频风格转绘、IPAdapter+ 增强风格参考、＋面部细节增强 | `realistic_vision_v5.1` · `v3_sd15_adapter` (LoRA) · `ip-adapter-plus_sd15` (IPA) _(+5)_ |
| 全能工作流-图像视频生成 | SVD 图像转视频、＋超分放大 | `svd_xt` · `4x-UltraSharp` (Up) _(+1)_ |
| 关键帧引导动画 | AnimateDiff 关键帧引导动画 | `ip-adapter-plus_sd15` (IPA) _(+2)_ |
| 利用controlnet生成图片和视频 | SVD 图像转视频、IPAdapter 图像风格参考 | `photon_v1` · `ip-adapter_sd15` (IPA) · `control_v11p_sd15_lineart` (CN) _(+4)_ |
| 动态红包封面SVD一键生成 | SVD 动态封面生成 | `svd_xt` |
| 动画生成器 | AnimateDiff 动画生成、IPAdapter 图像风格参考 | `305_744_945` · `ip-adapter_sd15` (IPA) _(+2)_ |
| 北一图生视频-低帧 | SVD 平滑图生视频 | `svd_xt_1_1` |
| 图片视角旋转器 | SVD 多角度视图旋转动画、ReActor 人脸替换、IPAdapter 图像风格参考 | `2580_4117_4838` · `ip-adapter_sd15` (IPA) _(+3)_ |
| 图片转视频 | AnimateDiff 视频风格转绘、ControlNet Tile 高清重绘、＋面部细节增强 | `GhostMix_V2.0` · `control_v11f1e_sd15_tile_fp16` (CN) · `2x-sudo-RealESRGAN` (Up) _(+6)_ |
| 图片转视频工作流 | SVD 图像转视频 | `svd_xt` |
| 图生视频 | AnimateDiff 动画生成、IPAdapter 图像风格参考 | `dreamshaper_8` · `ip-adapter_sd15` (IPA) _(+2)_ |
| 图生视频_最小闭环SVD工作流 | SVD 图生视频（基础教程） | `svd_xt_1_1` |
| 图生视频工作流 | SVD 图像转视频 | `svd_xt` |
| 图转视频_平滑 | SVD 平滑图生视频 | `svd_xt_1_1` |
| 基于IPAdapter的视频生成 | AnimateDiff 动画生成、IPAdapter 图像风格参考 | `meinamix_meinaV11` · `ip-adapter_sd15` (IPA) _(+2)_ |
| 基于SVD的图生视频 | SVD 图像转视频 | `svd_xt` |
| 基于稀疏控制网络的视频重绘 | AnimateDiff SparseCtrl 稀疏运动控制、ReActor 视频换脸、＋超分放大 | `0001semirealistic_v54` · `Gothpunk` (LoRA) · `control_v11f1e_sd15_tile_fp16` (CN) _(+11)_ |
| 多提示动画Gif | AnimateDiff 文本转 GIF 动图、ControlNet 引导图像生成 | `dreamshaper_8` · `v3_sd15_adapter` (LoRA) · `animateddiff_controlnet` (CN) _(+1)_ |
| 女孩的一生 | AnimateDiff 长序列叙事动画 | `3049_4621_5411` |
| 女孩的一生-带高清修复版 | AnimateDiff 长序列叙事动画 | `3049_4621_5411` |
| 完美的批处理_视频_图像工作流程 | AnimateDiff 动画生成、ReActor 视频换脸、IPAdapter 人脸参考生成 | `cuteheaven_v20` · `hip_sway_dancev1` (LoRA) · `ip-adapter-plus-face_sd15` (IPA) _(+14)_ |
| 小显存_自动化_无限时长_视频转绘制工作 | AnimateDiff 视频风格转绘、ControlNet 姿态控制生成 | `lcm-lora-sdv1-5` (LoRA) · `control_v11p_sd15_lineart` (CN) _(+2)_ |
| 小说推文分镜生成 | AnimateDiff 动画生成、IPAdapter 图像风格参考 | `683_3660_4305` · `ip-adapter_sd15` (IPA) _(+1)_ |
| 换脸换衣服加动作视频 | ReActor 视频换脸、AnimateDiff 视频风格转绘、IPAdapter FaceID 人脸一致性生成 | `add(1)` (LoRA) · `ip-adapter-faceid-plusv2_sd15` (IPA) · `control_v11p_sd15_openpose` (CN) _(+4)_ |
| 文字创意动画_中文版 | AnimateDiff 动画生成、IPAdapter 图像风格参考、＋UltimateSD 放大 | `DreamShaper XL_Turbo DPMpp SDE(…` · `Harrlogos XL - Finally, custom …` (LoRA) · `ip-adapter_sdxl` (IPA) _(+6)_ |
| 文字描述生成视频_可在线输出 | AnimateDiff 动画生成 | `majicMIX realistic(v7)` |
| 文字生视频 | AnimateDiff 动画生成 | `majicMIX realistic(v7)` |
| 文本生成动画gif工作流 | AnimateDiff 文本转 GIF 动图 | `蓝印花(V1.0)` |
| 文本转视频_SVD | SVD 图像转视频 | `svd_xt` _(+1)_ |
| 文生动画_高清修复 | AnimateDiff 动画生成 | `683_3660_4305` _(+1)_ |
| 文生图_图生视频_最小闭环SVD工作流 | SVD 图生视频（基础教程） | `svd_xt` _(+1)_ |
| 文生图生视频 | AnimateDiff 动画生成、ControlNet Tile 高清重绘、＋超分放大 | `1990sAnimeStyleLora_1` (LoRA) · `control_v11f1e_sd15_tile` (CN) · `lollypop` (Up) _(+4)_ |
| 文生视频 | SVD 图像转视频、＋面部细节增强、＋UltimateSD 放大 | `GhostXL(1.0-Baked VAE)` · `RealESRGAN_x4plus` (Up) _(+3)_ |
| 文生视频动画 | AnimateDiff 文字驱动视频 | `majicmixRealistic_v7` · `sd15_lcm_lora_rank1` (LoRA) _(+1)_ |
| 新手入门必看图片转视频 | SVD 图生视频（基础教程） | `svd` |
| 新手版_AD_批量提示词_可控动画 | AnimateDiff 动画生成 | `Cheese Daddy's Landscapes mix |…` |
| 新手版_图转视频_绘制运动轨迹 | DragNUWA 轨迹控制视频 | `dragnuwa-svd-pruned.fp16` |
| 无限循环_-_img2vid_AnimateD | AnimateDiff 视频风格转绘、ControlNet QR码特效、＋超分放大 | `juggernaut_reborn` · `AnimateLCM_sd15_t2v_lora` (LoRA) · `VIT-G (medium strength)` (IPA) _(+3)_ |
| 标准生成含LoRA工作流 | AnimateDiff 标准 LoRA 动画生成 | `ugaritMERGE_palestrom` · `pytorch_lora_weights` (LoRA) _(+1)_ |
| 根据提示词生成动画 | AnimateDiff 动画生成 | — |
| 流体素材引导动画 | AnimateDiff 视频风格转绘、IPAdapter+ 增强风格参考 | `1502_3868_4550` · `ip-adapter-plus_sd15` (IPA) _(+2)_ |
| 涂一笔_动起来 | SVD 图像转视频 | `svd_xt` |
| 潮流商品设计师 | SVD 图像转视频、IPAdapter+ 增强风格参考、＋UltimateSD 放大 | `revAnimated_v122(V1.0)` · `ip-adapter-plus_sd15` (IPA) · `control_v11f1p_sd15_depth` (CN) _(+3)_ |
| 照片跳舞工作流 | MagicAnimate 姿态驱动动画、ReActor 视频换脸、＋超分放大 | `diffusion_pytorch_model` · `RealESRGAN_x4plus` (Up) |
| 照片转视频_让你的图片动起来 | SVD 图像转视频 | `svd_xt` _(+1)_ |
| 狸花猫进化萨摩耶 | AnimateDiff 动画生成、IPAdapter 图像风格参考 | `Deliberate(v2)` · `ip-adapter_sd15` (IPA) _(+2)_ |
| 生成可控动画_基于DragNUWA实现 | DragNUWA 轨迹控制视频 | `dragnuwa-svd-pruned.fp16` |
| 生成景深感强的图像和视频 | SVD 图像转视频、IPAdapter 图像风格参考 | `photon_v1` · `ip-adapter_sd15` (IPA) _(+3)_ |
| 短片图生视频工作流 | SVD 平滑图生视频 | `svd_xt_1_1` |
| 稳定文生视频工作流 | DynamiCrafter 图像引导视频生成 | `Realistic Vision V6.0 B1 真实视觉 R…` _(+1)_ |
| 艺术字生成动画 | AnimateDiff 动画生成、IPAdapter 图像风格参考、＋UltimateSD 放大 | `DreamShaper XL_Turbo DPMpp SDE(…` · `Harrlogos XL - Finally, custom …` (LoRA) · `ip-adapter_sdxl` (IPA) _(+6)_ |
| 荒诞艺术动画 | AnimateDiff 动画生成 | `Unsettling_2.0-000002` (LoRA) _(+3)_ |
| 视频工作流 | SVD 图像转视频 | `svd_xt` |
| 视频扣人像 | AnimateDiff 视频风格转绘、RemBG 去背 | `833_4584_5364` |
| 视频换脸 | ReActor 视频换脸、AnimateDiff 视频风格转绘 | `833_4584_5364` _(+1)_ |
| 视频生成-Controlnet_IPAdapter_AnimateDiff | AnimateDiff 动画生成、IPAdapter+ 增强风格参考 | `0001semirealistic_v54` · `pytorch_lora_weights` (LoRA) · `ip-adapter-plus_sd15` (IPA) _(+10)_ |
| 视频生视频_AnimateDiff | AnimateDiff 视频风格转绘、IPAdapter+ 增强风格参考 | `epicrealism_pureEvolutionV5` · `no_bra_v20-10` (LoRA) · `ip-adapter-plus_sd15` (IPA) _(+6)_ |
| 视频转绘 | AnimateDiff 视频风格转绘、IPAdapter+ 增强风格参考 | `PLUS (high strength)` (IPA) · `control_v11f1e_sd15_tile` (CN) _(+2)_ |
| 视频转绘-AnimateDiff-ControlNet版 | AnimateDiff 视频风格转绘、ControlNet 姿态控制生成 | `add_detail` (LoRA) · `control_v11f1p_sd15_depth` (CN) _(+2)_ |
| 视频转绘-AnimateDiff简易版 | AnimateDiff 视频风格转绘、ControlNet 姿态控制生成 | `1102_2223_2644` · `control_v11f1p_sd15_depth` (CN) _(+1)_ |
| 视频转绘-AnimateDiff视频输入v1 | AnimateDiff 视频风格转绘、ControlNet 姿态控制生成 | `control_v11p_sd15_openpose` (CN) _(+2)_ |
| 视频转绘-AnimateDiff视频输入v2 | AnimateDiff 视频风格转绘、ControlNet Tile 高清重绘 | `control_v11f1e_sd15_tile_fp16` (CN) _(+3)_ |
| 视频转绘-AnimateDiff进化采样版 | AnimateDiff 视频风格转绘、ControlNet 姿态控制生成 | `revAnimated_v122EOL` · `LCM_LoRA_Weights_SD15` (LoRA) · `control_v11f1p_sd15_depth` (CN) _(+7)_ |
| 视频转绘-IPAdapter增强版 | 视频风格转绘、AnimateDiff SparseCtrl 稀疏运动控制、IPAdapter+ 增强风格参考 | `majicmixRealistic_v7` · `ip-adapter-plus_sd15` (IPA) · `control_v11p_sd15_openpose` (CN) _(+5)_ |
| 视频转绘_放大自用 | AnimateDiff 视频风格转绘、IPAdapter+ 增强风格参考、＋超分放大 | `墨幽︱二次元(v2)` · `赛博朋克室内设计_V1.0(赛博朋克室内设计_V1.0)` (LoRA) · `ip-adapter-plus_sd15` (IPA) _(+4)_ |
| 视频转绘换脸 | AnimateDiff 视频风格转绘、ReActor 视频换脸、IPAdapter 人脸参考生成 | `majicmix7` · `ip-adapter-plus-face_sd15` (IPA) · `GFPGANv1.4` (FR) _(+3)_ |
| 视频转视频 | AnimateDiff 视频风格转绘、ControlNet 姿态控制生成 | `majicMIX realistic(v7)` · `control_sd15_animal_openpose_fp16` (CN) _(+2)_ |
| 超逼真的换脸 | ReActor 人脸替换、SVD 图像转视频、＋超分放大 | `sd_xl_refiner_1.0_0.9vae` · `OpenPoseXL2` (CN) · `4x-UltraSharp` (Up) _(+3)_ |
| 静帧变视频SVD | SVD 图像转视频 | `svd_xt_image_decoder` |
| 首尾可控动画_RGB模式 | AnimateDiff SparseCtrl 稀疏运动控制 | `v3_sd15_adapter(v3)` (LoRA) _(+1)_ |
| 骨骼动画 | AnimateDiff 视频风格转绘、IPAdapter 图像风格参考 | `833_4584_5364` · `241_574_723` (LoRA) · `ip-adapter_sd15` (IPA) _(+3)_ |
| 高分辨率修复工作流 | AnimateDiff 视频风格转绘、IPAdapter 图像风格参考、＋超分放大 | `3Dmeinamix_meinaV11` · `ip-adapter_sd15` (IPA) · `control_v11f1e_sd15_tile` (CN) _(+5)_ |
| 龙战士动画 | AnimateDiff 动画生成、IPAdapter+ 增强风格参考 | `DreamShaper(8 LCM)` · `ip-adapter-plus_sd15` (IPA) · `control_v11f1e_sd15_tile` (CN) _(+1)_ |

## 🧑 AI换脸人像（71 个）

| 工作流文件 | 作用描述 | 主要模型 |
|-----------|---------|---------|
| 3D头像Photomaker | PhotoMaker 人像生成 | `crazycolorsv1.0` (LoRA) · `PhotoMaker` (PM) |
| 4k高清换脸 | ReActor 人脸替换、＋超分放大 | `RealESRGAN_x4plus` (Up) |
| AI摄影_V2.0 | InstantID 人像风格迁移、IPAdapter+ 增强风格参考、＋UltimateSD 放大 | `PLUS (high strength)` (IPA) · `TTPLANET_Controlnet_Tile_realis…` (CN) · `1xDeJPG_OmniSR` (Up) _(+3)_ |
| ControlNet-Canny内绘工作流 | ReActor 人脸替换、ControlNet 深度图引导生成、＋超分放大 | `realisticVisionV51_v51VAE` · `control_sd15_canny` (CN) · `ESRGAN_4x` (Up) _(+3)_ |
| FaceSwap_with_InstantID_IPAdapter_是一种基于主题风格参考图片的换脸技术 | 人脸替换/换脸、InstantID 人像风格迁移、IPAdapter+ 增强风格参考 | `dreamshaperXL_turboDpmppSDE` · `ip-adapter-plus_sdxl_vit-h` (IPA) · `control_instant_id_sdxl` (CN) _(+3)_ |
| InstantID实现人物一致性生成 | InstantID 人像风格迁移 | `turbovisionxlSuperFastXLBasedOn…` · `diffusion_pytorch_model` (CN) · `ip-adapter` (IID) _(+1)_ |
| InstantID肖像 | InstantID 人像风格迁移 | `controlnet` (CN) |
| InstantID肖像-InsightFace版 | InstantID 人像风格迁移 | `default` (CN) |
| MJ_换脸_放大 | ReActor 人脸替换、＋UltimateSD 放大 | `majicMIX realistic(v7)` · `Detail Tweaker LoRA (细节调整LoRA)(…` (LoRA) · `4x-UltraSharp` (Up) |
| MixAI摄影「老照片修复」 | ReActor 人脸替换、ControlNet 姿态控制生成 | `epicphotogasm_v4One4All(v4)` · `control_v11f1p_sd15_depth` (CN) _(+3)_ |
| PhotoMaker-不可用于商业用途 | PhotoMaker 人像生成 | `` (PM) |
| PhotoMaker_换脸工作流 | 人脸替换/换脸、PhotoMaker 人像生成 | `sd_xl_offset_example-lora_1.0` (LoRA) · `PhotoMaker` (PM) _(+1)_ |
| Q版-龙凤配 | ReActor 人脸替换、IPAdapter 人脸参考生成 | `ip-adapter-plus-face_sdxl_vit-h` (IPA) _(+2)_ |
| ReActor_肖像大师换脸_工作流 | ReActor 人脸替换、ControlNet 姿态控制生成、＋面部细节增强 | `XXMix_9realistic基础模型升级版(v1.0)` · `thibaud_xl_openpose` (CN) _(+3)_ |
| Rick一键人像摄影工作流 | InstantID 人像风格迁移 | `TurboVisionXL(V4.3.1)` · `diffusion_pytorch_model` (CN) · `ip-adapter` (IID) _(+1)_ |
| comfyui一键人像摄影工作流v3震撼来袭 | ReActor 人脸替换、InstantID 人像风格迁移 | `turbovisionxlSuperFastXLBasedOn…` · `diffusion_pytorch_model` (CN) · `ip-adapter` (IID) |
| instandid_换脸 | 人脸替换/换脸、InstantID 人像风格迁移 | `万享XL_超写实摄影(V6)` · `diffusion_pytorch_model` (CN) · `ip-adapter` (IID) |
| instantID_controlnet | InstantID 人像风格迁移、ControlNet 深度图引导生成 | `基础模型升级版YamersRealisticNSFW_v5TX…` · `control_instant_id_sdxl` (CN) · `ip-adapter` (IID) _(+1)_ |
| instantID人像迁移 | InstantID 人像风格迁移 | `turbovisionxlSuperFastXLBasedOn…` · `diffusion_pytorch_model` (CN) · `ip-adapter` (IID) _(+1)_ |
| instantid换脸匹配光影版 | 人脸替换/换脸、InstantID 人像风格迁移、＋UltimateSD 放大 | `Dream Tech XL | 筑梦工业XL(v4.0 - 向…` · `ttplanetSDXLControlnet_v20Fp16` (CN) · `4xNomos8kDAT` (Up) _(+3)_ |
| instant人像摄影工作流 | InstantID 人像风格迁移 | `TurboVisionXL(V4.3.1)` · `diffusion_pytorch_model` (CN) · `ip-adapter` (IID) _(+1)_ |
| ipadapter-faceid_v2 | ReActor 人脸替换、IPAdapter FaceID 人脸一致性生成 | `墨幽人造人(v1080-none)` · `LEOSAM's FilmGirl 胶片风 Film Grai…` (LoRA) · `ip-adapter-faceid-plusv2_sd15` (IPA) _(+3)_ |
| reactor | ReActor 人脸替换 | — |
| 一键换脸 | ReActor 人脸替换、＋UltimateSD 放大 | `墨幽人造人(v1080-none)` · `4x-UltraSharp` (Up) |
| 一键换脸_成人小孩都行_需要参考图 | ReActor 人脸替换、＋UltimateSD 放大 | `墨幽人造人(v1080-none)` · `4x-UltraSharp` (Up) |
| 一键换脸_生成相近风格图 | ReActor 人脸替换、ControlNet Tile 高清重绘 | `墨幽人造人(v1080-none)` · `JK lure dress JK战袍(NO.3)` (LoRA) · `control_v11f1e_sd15_tile` (CN) _(+3)_ |
| 一键生成服装 | ReActor 人脸替换、IPAdapter FaceID 人脸一致性生成、RemBG 去背 | `majicMIX realistic(v7)` · `ip-adapter-faceid-plusv2_sd15_l…` (LoRA) · `ip-adapter-faceid-plusv2_sd15` (IPA) _(+9)_ |
| 一键生成红白蓝三张证件照 | 证件照自动生成、ReActor 人脸替换、＋UltimateSD 放大 | `majicMIX realistic(v7)` · `4x-UltraSharp` (Up) |
| 万能工作流_换脸 | 人脸替换/换脸、InstantID 人像风格迁移、SUPIR 超分辨率放大 | `juggernautXL_v9-Lightning_4S_V9…` · `control_instant_id_sdxl` (CN) · `4x_foolhardy_Remacri` (Up) _(+1)_ |
| 人物动作背景个性化工作流 | ReActor 人脸替换、ControlNet 姿态控制生成、＋UltimateSD 放大 | `majicMIX realistic(v7)` · `GirlfriendMix_v1(v2.0)` (LoRA) · `control_v11p_sd15_openpose` (CN) _(+1)_ |
| 人物姿势识别_换脸_高清修复 | ReActor 人脸替换、ControlNet 姿态控制生成、＋UltimateSD 放大 | `DunhuangMix 敦煌 飞天 古风 (V1.1修剪版)` · `GirlfriendMix_v1(v2.0)` (LoRA) · `control_v11p_sd15_openpose` (CN) _(+1)_ |
| 人物转漫画风格 | PhotoMaker 人像生成 | `` (PM) |
| 人脸交换_匹配脸型 | ReActor 人脸替换、IPAdapter 人脸参考生成 | `realisticVisionV60B1_v60B1VAE` · `ip-adapter-plus-face_sd15` (IPA) · `control_v11p_sd15_canny` (CN) _(+5)_ |
| 人脸修复和reactor换脸 | ReActor 人脸替换、＋面部细节增强 | `majicMIX realistic(v7)` _(+1)_ |
| 任意换脸 | ReActor 人脸替换、＋超分放大 | `Realistic Vision V6.0 B1 真实视觉 R…` · `RealESRGAN_x4plus` (Up) |
| 你的专属Ai模特 | ReActor 人脸替换、ControlNet 姿态控制生成 | `epicrealism_naturalSinRC1VAE` · `control_v11p_sd15_canny` (CN) _(+3)_ |
| 卡通换脸 | ReActor 人脸替换、＋面部细节增强 | `majicMIX realistic(v7)` _(+1)_ |
| 发型设计师-SDXL | InstantID 人像风格迁移、ControlNet Tile 高清重绘、＋面部细节增强 | `墨幽人造人XL(v0.1)` · `control_v11f1e_sd15_tile` (CN) · `ip-adapter` (IID) _(+4)_ |
| 商业证件照 | 证件照自动生成、ReActor 人脸替换 | `FenrisXL(XL14.5)` · `ip-adapter_sdxl` (IPA) _(+1)_ |
| 图片换脸_高清画质 | ReActor 人脸替换、＋超分放大 | `RealESRGAN_x4plus` (Up) |
| 图片视频换脸-Reactor | ReActor 视频换脸 | — _(+1)_ |
| 图生四图 | ReActor 人脸替换、IPAdapter FaceID 人脸一致性生成 | `majicMIX realistic(v7)` · `浮世繁花(v1.2)` (LoRA) · `ip-adapter-faceid-plusv2_sd15` (IPA) _(+1)_ |
| 复刻加换脸 | ReActor 人脸替换、ControlNet 姿态控制生成 | `麦橘写实V7majicmixRealistic_v7` · `Ã¥ÂÂ°Ã©ÂÂªÃ¥Â¥ÂÃ§Â¼Â_V1` (LoRA) · `control_v11f1p_sd15_depth` (CN) _(+3)_ |
| 常用的一些 | ReActor 人脸替换、IPAdapter 人脸参考生成 | `2882_4423_5179` · `206_444_543` (LoRA) · `ip-adapter-plus-face_sd15` (IPA) _(+5)_ |
| 徐挺的换脸_高清修复 | ReActor 人脸替换、ControlNet Tile 高清重绘 | `majicMIX realistic(v7)` · `control_v11f1e_sd15_tile` (CN) · `4x-UltraSharp` (Up) |
| 批量换脸 | ReActor 人脸替换 | — |
| 换脸 | ReActor 人脸替换、＋超分放大 | `RealESRGAN_x4plus` (Up) |
| 换脸-高级文本编码放大版 | ReActor 人脸替换、＋UltimateSD 放大 | `墨幽人造人(v1080-none)` · `4x-UltraSharp` (Up) |
| 换脸_修手_放大 | ReActor 人脸替换、IPAdapter FaceID 人脸一致性生成、＋UltimateSD 放大 | `majicmixRealistic_betterV2V25` · `ip-adapter-faceid-plusv2_sd15` (IPA) · `control_sd15_inpaint_depth_hand…` (CN) _(+4)_ |
| 换脸_换动作_高清 | ReActor 人脸替换、ControlNet 姿态控制生成、＋UltimateSD 放大 | `DunhuangMix 敦煌 飞天 古风 (V1.1修剪版)` · `GirlfriendMix_v1(v2.0)` (LoRA) · `control_v11p_sd15_openpose` (CN) _(+1)_ |
| 换脸分辨率增加4倍 | ReActor 人脸替换、＋超分放大 | `RealESRGAN_x4plus` (Up) |
| 换脸工作流 | 人脸替换/换脸 | `codeformer` (FR) |
| 换脸工作流-Reactor版 | ReActor 人脸替换、＋超分放大 | `RealESRGAN_x4plus` (Up) |
| 换脸放大生成四张只用1羊毛 | ReActor 人脸替换、ControlNet Tile 高清重绘 | `majicMIX realistic(v7)` · `【麻瓜lora】身材调节器S-shape body(v1.0)` (LoRA) · `control_v11f1e_sd15_tile` (CN) _(+3)_ |
| 换装换脸换背景v2 | ReActor 人脸替换、IPAdapter FaceID 人脸一致性生成 | `majicMIX realistic(v7)` · `ip-adapter-faceid-plusv2_sd15_l…` (LoRA) · `ip-adapter-faceid-plusv2_sd15` (IPA) _(+7)_ |
| 文生图_换脸修复 | ReActor 人脸替换 | `majicMIX_realistic_麦橘写实_v7` |
| 旧照片修复_速度快_高还原度 | ReActor 人脸替换、ControlNet 姿态控制生成 | `epicphotogasm_v4One4All(v4)` · `control_v11f1p_sd15_depth` (CN) _(+3)_ |
| 旧照片恢复 | ReActor 人脸替换、ControlNet 姿态控制生成 | `epicphotogasm_x` · `control_v11f1p_sd15_depth` (CN) _(+3)_ |
| 时尚抽卡机2.0 | ReActor 人脸替换、＋面部细节增强 | `DreamShaper XL_Turbo DPMpp SDE(…` · `lcm_xl` (LoRA) · `GFPGANv1.4` (FR) _(+3)_ |
| 最佳的换脸工作流 | ReActor 人脸替换、ControlNet 姿态控制生成 | `dreamshaper_8` · `control_sd15_depth` (CN) _(+4)_ |
| 服装制作工作流V2 | ReActor 人脸替换、IPAdapter 图像风格参考、＋UltimateSD 放大 | `Juggernaut XL(v8+Rundiffusion)` · `ip-adapter_sdxl` (IPA) · `thibaud_xl_openpose` (CN) _(+2)_ |
| 照片修复 | ReActor 人脸替换、ControlNet 姿态控制生成 | `epicphotogasm_v4One4All(v4)` · `control_v11f1p_sd15_depth` (CN) _(+3)_ |
| 用你的照片生成毛绒玩具 | InstantID 人像风格迁移 | `dreamshaperXL_lightningDPMSDE` · `instanid.diffusion_pytorch_model` (CN) · `ip-adapter` (IID) |
| 电商一件换装完整修复版 | 虚拟换装、ReActor 人脸替换、IPAdapter FaceID 人脸一致性生成 | `majicmixRealistic_v7` · `ip-adapter-faceid-plusv2_sd15_lora` (LoRA) · `ip-adapter-faceid-plusv2_sd15` (IPA) _(+9)_ |
| 老吴顶级换脸车间 | ReActor 人脸替换、IPAdapter FaceID 人脸一致性生成 | `checkpoints_placeholder@0F2A9B4…` · `ip-adapter-faceid-plusv2_sd15` (IPA) _(+1)_ |
| 老照片修复-ControlNet版v1 | ReActor 人脸替换、ControlNet 姿态控制生成 | `epicphotogasm_v4One4All(v4)` · `control_v11f1p_sd15_depth` (CN) _(+3)_ |
| 老照片修复-ControlNet版v3 | ReActor 人脸替换、ControlNet 姿态控制生成 | `epicphotogasm_v4One4All(v4)` · `control_v11f1p_sd15_depth` (CN) _(+3)_ |
| 老照片修复by_dahai修订 | ReActor 人脸替换、ControlNet 姿态控制生成 | `majicmixRealistic_v7` · `control_v11f1p_sd15_depth_fp16` (CN) _(+3)_ |
| 视频换脸_转绘测试 | ReActor 视频换脸、ControlNet Tile 高清重绘 | `墨幽人造人(v1080-none)` · `【麻瓜lora】身材调节器S-shape body(v1.0)` (LoRA) · `control_v11f1e_sd15_tile` (CN) _(+3)_ |
| 证件照_换脸_换背景_换服装 | 证件照自动生成、ReActor 人脸替换、＋UltimateSD 放大 | `majicMIX alpha 麦橘男团(v2)` · `GirlfriendMix_v1(v2.0)` (LoRA) · `control_v11p_sd15_openpose` (CN) _(+1)_ |
| 高清放大-無山 | ReActor 人脸替换、＋UltimateSD 放大 | `majicMIX realistic(v7)` · `4x-UltraSharp` (Up) |

## 👗 AI电商换装（2 个）

| 工作流文件 | 作用描述 | 主要模型 |
|-----------|---------|---------|
| OOTDiffusion一键换装 | OOTDiffusion 虚拟换装 | — |
| OOTDiffusion换衣服学习笔记 | OOTDiffusion 虚拟换装 | — |

## ✂️ AI换背景抠图（63 个）

| 工作流文件 | 作用描述 | 主要模型 |
|-----------|---------|---------|
| AIX专业摄影3.0 | ControlNet 姿态控制生成、＋超分放大 | `majicMIX realistic(v7)` · `control_any3_openpose` (CN) · `4x-UltraSharp` (Up) _(+3)_ |
| AI摄影 | ControlNet 姿态控制生成、＋超分放大 | `majicMIX realistic(v7)` · `control_v11p_sd15_inpaint` (CN) · `4x-UltraSharp` (Up) _(+3)_ |
| CUTE_YOU使用一张照片创建你的卡通形象 | IPAdapter 人脸参考生成、ControlNet 姿态控制生成、＋面部细节增强 | `ip-adapter-plus-face_sdxl_vit-h` (IPA) · `OpenPoseXL2` (CN) _(+5)_ |
| IC-light实现电商换背景打光 | 背景替换、IPAdapter+ 增强风格参考、IC-Light 光影重打光 | `juggernautXL_v9-Lightning_4S_V9…` · `PLUS (high strength)` (IPA) · `control-lora-depth-rank256` (CN) _(+2)_ |
| Q版拜年照一键生成 | IPAdapter 人脸参考生成、ControlNet 姿态控制生成 | `samaritan3dCartoon_V3(SD1.5)` · `Concept Sliders: smiling笑(V1.0)` (LoRA) · `ip-adapter-plus-face_sdxl_vit-h` (IPA) _(+6)_ |
| SDXL_图片放大工作流 | 图像放大/超分辨率示例 | `yamer_realistic-v4` · `4x-UltraSharp` (Up) _(+2)_ |
| aix_摄影3.0 | ControlNet 姿态控制生成、＋超分放大 | `majicV7` · `control_v11p_sd15_inpaint` (CN) · `4x-UltraSharp` (Up) _(+3)_ |
| may-指定物体抠图_透明_自定义背景色 | SAM 语义分割/抠图 | — _(+1)_ |
| 一键抠图_简单型 | RemBG 自动去背景/抠图 | — |
| 一键换背景 | 背景替换、ControlNet Tile 高清重绘、RemBG 去背 | `chilloutmix_NiPrunedFp32Fix` · `control_v11f1e_sd15_tile` (CN) · `4x-UltraSharp` (Up) _(+4)_ |
| 一键换脸_IP-FaceID | 人脸替换/换脸、IPAdapter FaceID 人脸一致性生成、＋UltimateSD 放大 | `墨幽人造人(v1080-none)` · `ip-adapter-faceid-plusv2_sd15` (IPA) · `control_v11p_sd15_openpose` (CN) _(+2)_ |
| 一键更换背景 | 背景替换、ControlNet Canny 边缘引导 | `control-lora-canny-rank256` (CN) _(+1)_ |
| 一键生成黏土风格 | ControlNet 深度图引导生成 | `ReminiClay黏土风_SDXL_V1.0` · `diffusers_xl_depth_full` (CN) _(+2)_ |
| 个性化宠物贴纸 | IPAdapter 图像风格参考、ControlNet 深度图引导生成、RemBG 去背 | `DreamShaper XL_Turbo DPMpp SDE(…` · `Dry Paint Peel Style(SDXL)` (LoRA) · `ip-adapter_sdxl` (IPA) _(+4)_ |
| 产品合成摄影_增强在线形象和社交媒体参与 | ControlNet Tile 高清重绘、＋超分放大 | `majicMIX realistic(v7)` · `control_v11f1e_sd15_tile` (CN) · `RealESRGAN_x4plus` (Up) _(+3)_ |
| 产品组合摄影 | ControlNet Tile 高清重绘、＋超分放大 | `deliberate_v2` · `control_v11f1e_sd15_tile` (CN) · `RealESRGAN_x4plus` (Up) _(+3)_ |
| 人物一键多表情 | IPAdapter 图像风格参考、ControlNet 深度图引导生成 | `majicMIX realistic(v7)` · `ip-adapter_sd15` (IPA) · `control_v11f1p_sd15_depth` (CN) _(+4)_ |
| 人物及服饰保持_更换背景_场景融合_精细化处理 | 背景替换、IPAdapter+ 增强风格参考、RemBG 去背 | `majicMIX realistic(v7)` · `ip-adapter-plus_sd15` (IPA) · `control_v11f1e_sd15_tile` (CN) _(+7)_ |
| 人物及服饰保留_背景及氛围变化_高清放大 | IPAdapter+ 增强风格参考、ControlNet Tile 高清重绘、RemBG 去背 | `majicMIX realistic(v7)` · `ip-adapter-plus_sd15` (IPA) · `control_v11f1e_sd15_tile` (CN) _(+7)_ |
| 修改姿态 | IPAdapter 人脸参考生成、ControlNet 姿态控制生成 | `RealCartoon3D(V13)` · `ip-adapter-plus-face_sd15` (IPA) · `control_v11p_sd15_openpose` (CN) _(+5)_ |
| 写真摄影 | ControlNet 姿态控制生成、＋超分放大 | `majicMIX realistic(v7)` · `control_any3_openpose` (CN) · `4x-UltraSharp` (Up) _(+3)_ |
| 利用遮罩重绘任意物体 | IPAdapter+ 增强风格参考、＋超分放大 | `absolutereality_v181INPAINTING` · `ip-adapter-plus_sd15` (IPA) · `RealESRGAN_x4` (Up) _(+3)_ |
| 卡通换脸-四步基础版 | 人脸替换/换脸、IPAdapter 人脸参考生成 | `Samaritan 3d Cartoon(V4.0)` · `Concept Sliders: cartoon卡通化(V1.0)` (LoRA) · `ip-adapter-plus-face_sdxl_vit-h` (IPA) _(+7)_ |
| 发型大师 | ControlNet 姿态控制生成 | `majicmixRealistic_v7` · `control_v11p_sd15_openpose` (CN) _(+3)_ |
| 商品换背景工作流 | 背景替换、IPAdapter 图像风格参考、＋UltimateSD 放大 | `场景电商专业产品摄影，一键直出日用品、化妆品等_1.0` (LoRA) · `ip-adapter_sdxl_vit-h` (IPA) · `control-lora-depth-rank256` (CN) _(+8)_ |
| 头像漫改V2.0 | IPAdapter FaceID 人脸一致性生成、ControlNet Tile 高清重绘 | `niji-动漫二次元加强版-banyun(v1)` · `ip-adapter-faceid-plusv2_sd15` (IPA) · `control_v11f1e_sd15_tile` (CN) _(+3)_ |
| 局部重绘 | ControlNet Inpaint 精准重绘 | `checkpoints_placeholder@0F2A9B4…` · `control_v11p_sd15_inpaint` (CN) _(+2)_ |
| 布鲁文斯-家具风格转换 | IPAdapter+ 增强风格参考、ControlNet Tile 高清重绘、RemBG 去背 | `realisticVisionV60B1_v60B1VAE.s…` · `Twe(v1)` (LoRA) · `ip-adapter-plus_sd15` (IPA) _(+7)_ |
| 布鲁文斯-懒人常用节点 | IPAdapter+ 增强风格参考、ControlNet Tile 高清重绘、RemBG 去背 | `NwsjRealMix_基础模型升级版(v1.0)` · `FilmVelvia3` (LoRA) · `ip-adapter-plus_sd15` (IPA) _(+14)_ |
| 广告词云一键生成 | ControlNet Inpaint 精准重绘、RemBG 去背、＋超分放大 | `EpicDiffusion(1.1)` · `control_v11p_sd15_inpaint` (CN) _(+1)_ |
| 强势重绘工作流-BrushNet | BrushNet 精准笔刷重绘 | `Realistic Vision V6.0 B1(V5.0(V…` · `Glass Sculptures(v2.0 completel…` (LoRA) _(+1)_ |
| 批量抠图工作流 | RemBG 自动去背景/抠图 | — |
| 抠图 | ControlNet Tile 高清重绘 | `meinamix_meinaV11` · `control_v11f1e_sd15_tile` (CN) _(+3)_ |
| 拜年工作流 | IPAdapter 人脸参考生成、ControlNet 姿态控制生成 | `ip-adapter-plus-face_sdxl_vit-h` (IPA) · `sai_xl_canny_256lora` (CN) _(+3)_ |
| 换特定服装 | 虚拟换装、IPAdapter 图像风格参考 | `majicMIX realistic(v7)` · `ip-adapter_sd15` (IPA) _(+2)_ |
| 换脸换背景_Ipadapter_BrushNet_降低AI图片检测几率 | 人脸替换/换脸、IPAdapter+ 增强风格参考、BrushNet 笔刷区域重绘 | `墨幽人造人(v1080-none)` · `PLUS (high strength)` (IPA) · `control_v11p_sd15_openpose` (CN) _(+4)_ |
| 换装 | 虚拟换装、IPAdapter+ 增强风格参考、＋面部细节增强 | `majicMIX realistic(v7)` · `PLUS (high strength)` (IPA) _(+4)_ |
| 提示词换背景_TILE修复 | 背景替换、ControlNet Tile 高清重绘、RemBG 去背 | `DgirlV2.1-真实质感强化(V3.0)` · `control_v11f1e_sd15_tile` (CN) · `4x-UltraSharp` (Up) _(+4)_ |
| 更换背景-無山 | 背景替换、ControlNet Tile 高清重绘、RemBG 去背 | `DgirlV2.1-真实质感强化(V3.0)` · `control_v11f1e_sd15_tile` (CN) · `4x-UltraSharp` (Up) _(+4)_ |
| 更改产品照片的背景 | ControlNet Tile 高清重绘、＋超分放大 | `deliberate_v2` · `control_v11f1e_sd15_tile` (CN) · `RealESRGAN_x4plus` (Up) _(+3)_ |
| 替换背景 | 背景替换、ControlNet 姿态控制生成、RemBG 去背 | `2716_4254_4991` · `1998_3476_4086` (LoRA) · `control_v11p_sd15_lineart` (CN) _(+2)_ |
| 海报设计 | ControlNet 姿态控制生成、RemBG 去背 | `realisticVisionV60B1_v60B1VAE` · `control_v11f1p_sd15_depth` (CN) _(+4)_ |
| 灵仙儿和二狗子AI摄影小助手1.0版 | IPAdapter FaceID 人脸一致性生成、ControlNet 姿态控制生成、＋超分放大 | `majicMIX realistic 麦橘写实_v6` · `ip-adapter-faceid_sd15_lora` (LoRA) · `ip-adapter-faceid_sd15` (IPA) _(+7)_ |
| 無山-换背景 | 背景替换、ControlNet Canny 边缘引导 | `majicMIX realistic(v7)` · `control_v11p_sd15_canny` (CN) _(+1)_ |
| 生成透明背景素材工作流 | Layered Diffusion 透明背景生成 | `Starlight XL 星光 Animated(v3.0)` |
| 电商产品拍摄 | IPAdapter+ 增强风格参考、RemBG 去背 | `ip-adapter-plus_sd15` (IPA) _(+1)_ |
| 电商产品换背景 | 背景替换、IPAdapter+ 增强风格参考、RemBG 去背 | `juggernautXL_v9-Lightning_4S_V9…` · `PLUS (high strength)` (IPA) · `control-lora-depth-rank256` (CN) _(+1)_ |
| 电商产品通用工作流_自制修正 | IPAdapter+ 增强风格参考、ControlNet Tile 高清重绘、RemBG 去背 | `majicMIX realistic(v7)` · `ip-adapter-plus_sd15` (IPA) · `control_sd15_depth_anything` (CN) _(+6)_ |
| 电商换商品图片 | ControlNet Tile 高清重绘 | `电商场景 l 简约中式_v1.1` (LoRA) · `control_v11f1e_sd15_tile` (CN) · `ESRGAN_4x` (Up) _(+4)_ |
| 疯狂T恤印花机 | T恤/服装印花生成、RemBG 去背 | `ghostmix_v20Bakedvae` |
| 真人头像转绘二次元 | IPAdapter 人脸参考生成、RemBG 去背 | `ReV Animated(v1.2.2)` · `中国風です Lora(v1.0)` (LoRA) · `ip-adapter-plus-face_sd15` (IPA) _(+1)_ |
| 移除背景_透明背景 | RemBG 自动去背景/抠图 | — _(+3)_ |
| 简易换装工作流 | 虚拟换装、IPAdapter+ 增强风格参考、＋超分放大 | `majicMIX realistic(v7)` · `abel帅哥，网红，男脸3(0.1)` (LoRA) · `ip-adapter-plus_sd15` (IPA) _(+5)_ |
| 自动扣像_文生图背景替换 | ControlNet Canny 边缘引导 | `majicMIX realistic(v7)` · `control_v11p_sd15_canny` (CN) _(+1)_ |
| 自定义服装背景_多重放大增加细节v1 | ControlNet Tile 高清重绘 | `majicMIX realistic(v7)` · `meidusa(1)` (LoRA) · `ip-adapter-plus_sd15` (IPA) _(+6)_ |
| 衣服测试 | ControlNet 姿态控制生成 | `majicMIX realistic(v7)` · `control_v11p_sd15_openpose` (CN) _(+1)_ |
| 设计师全能工具包 | ControlNet 线稿引导生成、＋面部细节增强、＋UltimateSD 放大 | `realisticVisionV60B1_v60B1VAE` · `control_v11p_sd15_lineart_fp16` (CN) · `4x-UltraSharp` (Up) _(+4)_ |
| 证件照_v2.1 | 证件照自动生成、IPAdapter+ 增强风格参考、BrushNet 笔刷区域重绘 | `juggernautXL_v9Rdphoto2Lightning` · `PLUS (high strength)` (IPA) · `control-lora-openposeXL2-rank256` (CN) _(+7)_ |
| 超级写真生成器 | ControlNet 姿态控制生成、＋超分放大 | `majicMIX realistic(v7)` · `control_any3_openpose` (CN) · `4x-UltraSharp` (Up) _(+3)_ |
| 透明素材生成工作流 | Layered Diffusion 透明背景生成、＋面部细节增强 | `RealVisXL V2.0(V2.0 (BakedVAE))` _(+2)_ |
| 颜色变化 | ControlNet 线稿引导生成 | `dreamshaper_8` · `GoodHands-beta2` (LoRA) · `control_v11p_sd15_lineart` (CN) _(+2)_ |
| 龙年大吉头像 | IPAdapter 人脸参考生成、ControlNet 姿态控制生成 | `Samaritan 3d Cartoon(V4.0)` · `Concept Sliders: cartoon卡通化(V1.0)` (LoRA) · `ip-adapter-plus-face_sdxl_vit-h` (IPA) _(+7)_ |
| 龙飞凤舞头像 | IPAdapter 人脸参考生成、ControlNet 姿态控制生成 | `Samaritan 3d Cartoon(V4.0)` · `Concept Sliders: cartoon卡通化(V1.0)` (LoRA) · `ip-adapter-plus-face_sdxl_vit-h` (IPA) _(+7)_ |

## 🔧 AI画质修复（130 个）

| 工作流文件 | 作用描述 | 主要模型 |
|-----------|---------|---------|
| 2D_to_3D_2D转3D | IPAdapter+ 增强风格参考、ControlNet 线稿引导生成、＋UltimateSD 放大 | `(风格)盲盒玩偶(V1)` · `ip-adapter-plus_sd15` (IPA) · `control_v11p_sd15_lineart` (CN) _(+2)_ |
| 2d转3d-ip形象 | ControlNet 线稿引导生成、＋超分放大 | `helloip3dV13(V13E)` · `KIDS ILLUSTRATION(COOLKIDS V2)` (LoRA) · `control_v11p_sd15_lineart` (CN) _(+3)_ |
| 2d转真人 | ControlNet Tile 高清重绘、＋面部细节增强 | `XXMix_9realistic(v4.0)` · `control_v11f1e_sd15_tile` (CN) · `RealESRGAN_x4plus` (Up) _(+2)_ |
| 2种无损高清放大工作流 | ControlNet Tile 高清重绘 | `DreamShaper XL_Turbo DPMpp SDE(…` · `Twe(v1)` (LoRA) · `control_v11f1e_sd15_tile` (CN) _(+4)_ |
| 3D动画 | Zero123 多角度三维视图、IPAdapter+ 增强风格参考、＋面部细节增强 | `stable_zero123` · `ip-adapter-plus_sdxl_vit-h` (IPA) · `control-lora-canny-rank256` (CN) _(+5)_ |
| 4种局部重绘 | ControlNet Inpaint 精准重绘 | `371_928_1178` · `control_v11p_sd15_inpaint` (CN) |
| 4种局部重绘工作流分享_最新 | ControlNet Inpaint 精准重绘 | `CounterfeitV25_25` · `control_v11p_sd15_inpaint` (CN) _(+1)_ |
| AI摄影_超写实 | IPAdapter FaceID 人脸一致性生成、ControlNet Tile 高清重绘 | `【SD1.5】epicrealism_naturalSinRC…` · `ip-adapter-faceid_sdxl_lora` (LoRA) · `ip-adapter-faceid_sdxl` (IPA) _(+5)_ |
| AI虚拟摄影v2.4_研学版 | IPAdapter 人脸参考生成、ControlNet 姿态控制生成、＋面部细节增强 | `epicrealism_v10-inpainting` · `PLUS FACE (portraits)` (IPA) · `control_v11p_sd15_openpose` (CN) _(+7)_ |
| AI造字工作流 | ControlNet 深度图引导生成、＋UltimateSD 放大 | `动漫ReVAnimated_v1.1` · `control_v11f1p_sd15_depth` (CN) · `RealESRGAN_x4plus` (Up) _(+2)_ |
| Dall-E_3_必应_逼真模型图像增强器 | Fooocus Inpaint 智能重绘 | `newrealityxlAllInOne_21` |
| IPAdapter_WD14_图片放大 | IPAdapter 图像风格参考、＋UltimateSD 放大 | `juggernautXL_v7Rundiffusion` · `ip-adapter_sdxl` (IPA) · `4x-UltraSharp` (Up) _(+3)_ |
| Ink_scenery_Art_-_SD | UltimateSD 高清放大 | `SD15_NoosPhere_v42` · `4x_NMKD-Superscale-SP_178000_G` (Up) _(+1)_ |
| Midjourney本地版 | UltimateSD 高清放大、＋面部细节增强 | `playground 2.5(v2.5)` · `4x-UltraSharp` (Up) _(+1)_ |
| MixAI一键自动扩图 | 图像外扩 (Outpainting)、IPAdapter 图像风格参考 | `DreamShaper XL_Turbo DPMpp SDE(…` · `ip-adapter_sdxl_vit-h` (IPA) _(+1)_ |
| Playground_V2.5 | Playground V2.5 图像生成、＋超分放大 | `Playground(v2.5)` · `4x-UltraSharp` (Up) |
| SD1.5_文生图_面部修复_高清修复 | UltimateSD 高清放大、＋面部细节增强 | `henmixReal_v5c` · `Supergirl_DCfilm` (LoRA) · `8x_NMKD-Superscale_150000_G` (Up) _(+3)_ |
| SDXL_inpaint_SD15 | 局部区域重绘 (Inpaint) | `sd_xl_base_1.0` _(+4)_ |
| SDXL_高分辨率修复 | UltimateSD 高清放大 | `juggernautXL_v7Rundiffusion` · `4x-UltraSharp` (Up) _(+1)_ |
| SUPIR_V2 | SUPIR 超分辨率放大 | — |
| SUPIR_超级高清修复 | SUPIR 超分辨率放大 | `4x-UltraSharp` (Up) |
| SUPIR图像放大 | SUPIR 超分辨率放大 | — |
| TILE高清放大_增加细节 | ControlNet Tile 高清重绘、＋超分放大 | `majicMIX realistic(v7)` · `control_v11f1e_sd15_tile` (CN) · `4x-UltraSharp` (Up) |
| T恤定制 | T恤/服装印花生成、IPAdapter 图像风格参考 | `turbovisionxlSuperFastXLBasedOn…` · `ip-adapter_sdxl` (IPA) _(+2)_ |
| XL局部重绘扩图二合一 | 图像外扩 (Outpainting)、IPAdapter+ 增强风格参考 | `ip-adapter-plus_sdxl_vit-h` (IPA) _(+1)_ |
| ai摄影助手 | IPAdapter 人脸参考生成、ControlNet Tile 高清重绘、＋面部细节增强 | `epiCRealism(pure Evolution-inpa…` · `ip-adapter-plus-face_sd15` (IPA) · `control_v11f1e_sd15_tile` (CN) _(+8)_ |
| compare_upscale_models | 图像放大/超分辨率示例 | `4x-UltraSharp` (Up) _(+3)_ |
| denoise_impact_on_pixel | 图像放大/超分辨率示例 | `v1-5-pruned-emaonly` · `4x_foolhardy_Remacri` (Up) _(+1)_ |
| fooocus_重绘扩图 | 图像外扩 (Outpainting) | `juggernautXL_v7Rundiffusion(V7)` |
| inpaint | 局部区域重绘 (Inpaint) | `dreamshaper_8` _(+2)_ |
| may-视图转绘_一致性高 | IPAdapter 图像风格参考、ControlNet 线稿引导生成、＋超分放大 | `helloip3dV13(V13E)` · `大概是盲盒(blindbox_v1_mix)` (LoRA) · `ip-adapter_sd15` (IPA) _(+5)_ |
| may三视图zero123 | Zero123 多角度三维视图、ControlNet Tile 高清重绘、＋超分放大 | `helloip3dV13(V13E)` · `KIDS ILLUSTRATION(COOLKIDS V2)` (LoRA) · `control_v11f1e_sd15_tile` (CN) _(+4)_ |
| may任意角度视图zero123 | Zero123 多角度三维视图、ControlNet Tile 高清重绘、＋超分放大 | `helloip3dV13(V13E)` · `KIDS ILLUSTRATION(COOLKIDS V2)` (LoRA) · `control_v11f1e_sd15_tile` (CN) _(+4)_ |
| may手稿转3d渲染 | ControlNet 线稿引导生成、＋超分放大 | `helloip3dV13(V13E)` · `KIDS ILLUSTRATION(COOLKIDS V2)` (LoRA) · `control_v11p_sd15_lineart` (CN) _(+3)_ |
| minecraft二维码生成 | 艺术二维码生成、ControlNet QR码特效、＋UltimateSD 放大 | `Disney Pixar Cartoon type B_v1.…` · `control_v1p_sd15_qrcode_monster_v2` (CN) · `4x-UltraSharp` (Up) |
| multiple_outpaints | 图像外扩 (Outpainting) | `dreamshaper_8` _(+2)_ |
| outpaint | 图像外扩 (Outpainting) | `sd-v1-5-inpainting` _(+2)_ |
| outpaint_seam_fix_SDXL | 图像外扩 (Outpainting) | `sd_xl_base_1.0` _(+1)_ |
| playgroundv2.5一键出图 | Playground V2.5 图像生成、＋超分放大 | `Playground(v2.5)` · `4x_NMKD-Superscale-SP_178000_G` (Up) |
| upscale_by_model | 图像放大/超分辨率示例 | `v1-5-pruned-emaonly` · `4x-UltraSharp` (Up) _(+1)_ |
| 一键商品打光 | IC-Light 光影控制生成、BrushNet 笔刷区域重绘 | `majicMIX realistic(v7)` · `PLUS (high strength)` (IPA) · `control_v11p_sd15_canny` (CN) |
| 一键扩图_Outpainting | 图像外扩 (Outpainting)、IPAdapter 图像风格参考 | `DreamShaper XL_Turbo DPMpp SDE(…` · `ip-adapter_sdxl_vit-h` (IPA) _(+1)_ |
| 一键换装 | 虚拟换装、ControlNet Inpaint 精准重绘 | `majicMIX realistic(v7)` · `control_v11p_sd15_inpaint` (CN) |
| 一键生成灰度图_深度图_浮雕图 | ControlNet Tile 高清重绘、＋超分放大 | `Deliberate_v5 (SFW)` · `GeekSGrayScale` (LoRA) · `control_v11f1e_sd15_tile` (CN) _(+3)_ |
| 三视图 | IPAdapter+ 增强风格参考、ControlNet Tile 高清重绘、＋面部细节增强 | `ReVAnimated_v122_V122(V1.22)` · `ip-adapter-plus_sd15` (IPA) · `control_v11f1e_sd15_tile` (CN) _(+6)_ |
| 两图人物合并 | IPAdapter+ 增强风格参考、ControlNet 线稿引导生成、＋超分放大 | `192_3750_4424` · `ip-adapter-plus_sd15` (IPA) · `control_v11p_sd15_lineart` (CN) _(+3)_ |
| 产品3D工作流 | Zero123 多角度三维视图、IPAdapter+ 增强风格参考、＋面部细节增强 | `3D效果sdvn53dcutewave_v10` · `LCM_LoRA_Weights_SD15` (LoRA) · `ip-adapter-plus_sd15` (IPA) _(+5)_ |
| 产品换背景 | 背景替换、ControlNet 深度图引导生成 | `leosamsHelloworld基础模型升级版真实亚洲艺术C…` · `control-lora-canny-rank256` (CN) _(+1)_ |
| 人脸_衣服 | IPAdapter 图像风格参考、＋超分放大 | `majicMIX realistic(v7)` · `VIT-G (medium strength)` (IPA) · `RealESRGAN_x4plus_anime_6B` (Up) _(+2)_ |
| 保持人物脸型_头发及姿势_更换照片主题分格和背景 | IPAdapter+ 增强风格参考、ControlNet 姿态控制生成、＋超分放大 | `majicMIX realistic(v7)` · `ip-adapter-plus_sd15` (IPA) · `control_v11p_sd15_openpose` (CN) _(+2)_ |
| 修复脸部_两种放大图像工作流 | UltimateSD 高清放大、＋面部细节增强 | `darkSushiMixMix_225D` · `ESRGAN_4x` (Up) _(+5)_ |
| 像素级图片放大 | 图像放大/超分辨率示例 | `dreamshaper_8` · `4x_foolhardy_Remacri` (Up) _(+1)_ |
| 创意_文字生成 | ControlNet 深度图引导生成、＋UltimateSD 放大 | `动漫ReVAnimated_v1.1` · `control_v11f1p_sd15_depth` (CN) · `RealESRGAN_x4plus` (Up) _(+2)_ |
| 参考人物和背景生图 | IPAdapter+ 增强风格参考、ControlNet 姿态控制生成、＋超分放大 | `majicMIX realistic(v7)` · `ip-adapter-plus_sd15` (IPA) · `control_v11p_sd15_openpose` (CN) _(+2)_ |
| 参考图片生成上传照片的风格的人像 | IPAdapter+ 增强风格参考、ControlNet 姿态控制生成、＋超分放大 | `majicMIX realistic(v7)` · `ip-adapter-plus_sd15` (IPA) · `control_v11p_sd15_openpose` (CN) _(+2)_ |
| 古风仙侠 | IPAdapter FaceID 人脸一致性生成、＋超分放大 | `南柯一梦丨YUEMIX(V1.0)` · `ip-adapter-faceid-plusv2_sd15_l…` (LoRA) · `ip-adapter-faceid-plusv2_sd15` (IPA) _(+4)_ |
| 告别手崩脸崩 | ControlNet 姿态控制生成、＋面部细节增强 | `majicMIX realistic 麦橘写实_v7` · `muuu之比基尼2_1.0` (LoRA) · `control_sd15_inpaint_depth_hand…` (CN) _(+5)_ |
| 图片放大-采样器_像素 | 模型超分放大 | `majicMIX realistic(v7)` · `RealESRGAN_x4plus` (Up) |
| 图片放大与细节修复 | 模型超分放大 | `dreamshaper_8` · `4x-UltraSharp` (Up) · `GFPGANv1.4` (FR) _(+3)_ |
| 图片高清化 | UltimateSD 高清放大 | `cyberrealistic_v33` · `SDXLrender_v2.0` (LoRA) · `4x_foolhardy_Remacri` (Up) |
| 基于LCM的实时窗口重绘 | ControlNet Tile 高清重绘、＋面部细节增强、＋超分放大 | `meinamix_meinaV11` · `C4D渲染风格（Q版）_v1.23` (LoRA) · `control_v11f1e_sd15_tile` (CN) _(+5)_ |
| 外扩图片最小闭环工作流 | 图像外扩 (Outpainting) | `v2-0_512-inpainting-ema` |
| 多视图工作流 | Zero123 多角度三维视图、＋UltimateSD 放大 | `stable_zero123` · `blindbox_V1Mix` (LoRA) · `BSRGAN` (Up) _(+1)_ |
| 多风格室内设计生成 | 室内/建筑效果图生成、IPAdapter+ 增强风格参考、＋UltimateSD 放大 | `398_3019_3598` · `ip-adapter-plus_sd15` (IPA) · `control_v11p_sd15_mlsd` (CN) _(+2)_ |
| 大脑袋大可爱_头像转绘 | IPAdapter FaceID 人脸一致性生成、＋面部细节增强、＋UltimateSD 放大 | `bluePencilXL_v200` · `ip-adapter-faceid_sdxl` (IPA) · `4xNomos8kSCHAT-L` (Up) _(+4)_ |
| 完美换脸下背景服装主题更换 | 人脸替换/换脸、IPAdapter+ 增强风格参考、＋超分放大 | `majicMIX realistic(v7)` · `ip-adapter-plus_sd15` (IPA) · `control_v11p_sd15_openpose` (CN) _(+2)_ |
| 室内装修实时渲染 | ControlNet 深度图引导生成、＋超分放大 | `sd_xl_base_1.0` · `lcm-lora-sdv1-5` (LoRA) · `SDXL_canny` (CN) _(+4)_ |
| 室内设计_户外设计 | 室内/建筑效果图生成、IPAdapter 图像风格参考、＋UltimateSD 放大 | `ip-adapter_sd15` (IPA) · `control_v11p_sd15_mlsd_fp16` (CN) · `ESRGAN_4x` (Up) _(+1)_ |
| 将图像转换为线稿 | IPAdapter 人脸参考生成、ControlNet 深度图引导生成、＋超分放大 | `sd_xl_base_1.0` · `ip-adapter-plus-face_sdxl_vit-h` (IPA) · `t2i-adapter-depth-zoe-sdxl-1.0-…` (CN) _(+5)_ |
| 布鲁文斯-字体生成 | ControlNet 深度图引导生成、＋超分放大 | `AlbedoBase XL(v2.0)` · `Mech_Dystopia_Style_基础模型升级版(SDXL)` (LoRA) · `sai_xl_depth_256lora` (CN) _(+1)_ |
| 建筑实时生成同步建模软件 | ControlNet Tile 高清重绘、＋超分放大 | `城市设计大模型 _ UrbanDesign_v7` · `pytorch_lora_weights _15` (LoRA) · `control_v11f1e_sd15_tile` (CN) _(+3)_ |
| 徐挺的修图流程 | ControlNet Tile 高清重绘、＋超分放大 | `2558_4095_4814` · `control-lora-recolor-rank256` (CN) · `ESRGAN_4x` (Up) _(+3)_ |
| 微观世界 | 微观世界创意风格生成、＋超分放大 | `SDXL_crystalClearXL_ccxl` · `4x-UniScaleV2_Sharp` (Up) |
| 扩图_2步扩图 | 图像外扩 (Outpainting)、ControlNet Inpaint 精准重绘、＋UltimateSD 放大 | `DreamShaper(8)` · `control_v11p_sd15_inpaint` (CN) · `4x-UltraSharp` (Up) |
| 换服装换背景 | 虚拟换装、ControlNet 姿态控制生成、＋超分放大 | `chilloutmix_NiPrunedFp16Fix(chi…` · `skin_tone_slider_v1` (LoRA) · `control_v11p_sd15_openpose` (CN) _(+5)_ |
| 换衣试装 | 虚拟换装、IPAdapter+ 增强风格参考、＋超分放大 | `DreamShaper(8)` · `ip-adapter-plus_sd15` (IPA) · `control_v11p_sd15_openpose` (CN) _(+2)_ |
| 换装_ipadapterV2.0_修手-学习笔记 | 虚拟换装、IPAdapter 图像风格参考 | `majicMIX realistic(v7)` · `STANDARD (medium strength)` (IPA) · `control_sd15_inpaint_depth_hand…` (CN) _(+3)_ |
| 放大模型_seg手部维修 | ControlNet 姿态控制生成、＋UltimateSD 放大 | `majicmixRealistic_v7` · `Zenpainting l 禅意插画_v1.0` (LoRA) · `control_v11p_sd15_openpose` (CN) _(+6)_ |
| 文字-二维码等图形生成 | 艺术二维码生成、ControlNet QR码特效、＋UltimateSD 放大 | `2287_3803_4481` · `control_v1p_sd15_qrcode_monster` (CN) · `4x-UltraSharp` (Up) |
| 文生图_姿势_修复放大 | ControlNet 姿态控制生成、＋面部细节增强、＋UltimateSD 放大 | `majicMIX realistic 麦橘写实_v7` · `control_v11p_sd15_openpose` (CN) · `4xNomos8kDAT` (Up) _(+3)_ |
| 文生图通用工作流 | IPAdapter FaceID 人脸一致性生成、ControlNet 姿态控制生成、＋面部细节增强 | `墨幽人造人(v1080-none)` · `Twe(v1)` (LoRA) · `ip-adapter-faceid-plusv2_sd15` (IPA) _(+11)_ |
| 新手入门必看局部重绘 | 局部区域重绘 (Inpaint) | `Ink(V5[Prt-RE])` _(+1)_ |
| 无损放大工作流 | ControlNet Tile 高清重绘 | `DreamShaper XL_Turbo DPMpp SDE(…` · `Twe(v1)` (LoRA) · `control_v11f1e_sd15_tile` (CN) _(+4)_ |
| 无需提示词提升图片质量 | IPAdapter+ 增强风格参考、ControlNet Tile 高清重绘 | `epicphotogasm_lastUnicorn` · `LCM.SD15_lora_weights` (LoRA) · `ip-adapter-plus_sd15` (IPA) _(+3)_ |
| 旧照片重生-对模糊的单色照片进行修复和重新上色 | ControlNet Tile 高清重绘、＋超分放大 | `foddaxlPhotorealism_v60` · `control-lora-recolor-rank256` (CN) · `RealESRGAN_x4` (Up) _(+3)_ |
| 时尚摄影师 | IPAdapter 人脸参考生成、ControlNet 深度图引导生成、＋面部细节增强 | `sd_xl_turbo_1.0_fp16` · `ip-adapter-plus-face_sdxl_vit-h` (IPA) · `control-lora-depth-rank128` (CN) _(+5)_ |
| 时尚摄影师-摄影棚流程版 | IPAdapter 人脸参考生成、ControlNet 深度图引导生成、＋面部细节增强 | `MOHAWK_v18VAEBaked` · `ip-adapter-plus-face_sdxl_vit-h` (IPA) · `control-lora-depth-rank128` (CN) _(+4)_ |
| 景观图高清重绘 | ControlNet 深度图引导生成、＋UltimateSD 放大 | `realisticVisionV51_v51VAE` · `control_depth-fp16` (CN) · `1x_DeBLR` (Up) _(+3)_ |
| 更换人物照片的背景和服装 | 人物背景替换、ControlNet 姿态控制生成、＋超分放大 | `chilloutmix_NiPrunedFp16Fix(chi…` · `skin_tone_slider_v1` (LoRA) · `control_v11p_sd15_openpose` (CN) _(+5)_ |
| 梦想改造家 | IPAdapter+ 增强风格参考、ControlNet 引导图像生成、＋UltimateSD 放大 | `DreamShaper(8)` · `ip-adapter-plus_sd15` (IPA) · `control_v11p_sd15_mlsd` (CN) _(+2)_ |
| 毛坯房_LOGO转变渲染 | IPAdapter+ 增强风格参考、ControlNet 引导图像生成、＋UltimateSD 放大 | `DreamShaper(8)` · `ip-adapter-plus_sd15` (IPA) · `control_v11p_sd15_mlsd` (CN) _(+2)_ |
| 毛坯房转渲染图V2.1 | IPAdapter+ 增强风格参考、ControlNet 引导图像生成、＋UltimateSD 放大 | `1-老王_ARCH_MIX_V0.5(0.5)` · `ip-adapter-plus_sd15` (IPA) · `control_v11p_sd15_mlsd` (CN) _(+2)_ |
| 添加服装 | 服装虚拟穿戴 | `analogMadness_v60` |
| 照片生成卡通人像 | IPAdapter FaceID 人脸一致性生成、＋超分放大 | `Samaritan 3d Cartoon(v1.0)` · `3D cartoon avatar(v1.0)` (LoRA) · `ip-adapter-faceid-plusv2_sd15` (IPA) _(+4)_ |
| 照片生成图片 | IPAdapter FaceID 人脸一致性生成 | `majicMIX realistic(v7)` · `ip-adapter-faceid-plusv2_sd15` (IPA) _(+3)_ |
| 照片肖像放大器 | ControlNet 深度图引导生成、＋UltimateSD 放大 | `realisticVisionV51_v51VAE` · `control_canny-fp16` (CN) · `4xNomos8kHAT-L_otf` (Up) _(+3)_ |
| 珠宝制作灵感生成器 | 珠宝/首饰设计生成 | `crystalClearXL_ccxl` · `add-detail-xl` (LoRA) · `4x-UltraSharp` (Up) |
| 珠宝设计专用_从线稿到实物 | 珠宝/首饰设计生成、ControlNet Canny 边缘引导 | `真实感Crystal Clear XL_CCXL(xl)` · `光效科幻场景 light effect sci-fi scen…` (LoRA) · `diffusers_xl_canny_full` (CN) _(+1)_ |
| 电商服装更换 | IPAdapter+ 增强风格参考、＋面部细节增强、＋UltimateSD 放大 | `dreamshaperXL_v21TurboDPMSDE` · `PLUS (high strength)` (IPA) · `4x-UltraSharp` (Up) _(+3)_ |
| 皮克斯风格画作 | ControlNet 引导图像生成、＋面部细节增强、＋UltimateSD 放大 | `0.SDXL-DIBUJOCHEYENNE_v12` · `DetailedEyes_V3` (LoRA) · `control-lora-sketch-rank128-met…` (CN) _(+10)_ |
| 真人转2.5D_tile高清 | IPAdapter+ 增强风格参考、ControlNet Tile 高清重绘 | `动漫ReVAnimated_v1.1.safetensors(…` · `3D rendering style(3DMM_V12)` (LoRA) · `ip-adapter-plus_sd15` (IPA) _(+5)_ |
| 科技感二维码生成器 | 艺术二维码生成、ControlNet QR码特效、＋UltimateSD 放大 | `中庸无为 | PoetAlmightyMix_2.5D(V1.0)` · `control_v1p_sd15_qrcode_monster` (CN) · `4x-UltraSharp` (Up) |
| 移除物体_RemoveObject | Fooocus Inpaint 智能重绘 | `dreamshaperXL_v21TurboDPMSDE` |
| 稳定五官的图像生成 | IPAdapter FaceID 人脸一致性生成、＋超分放大 | `majicMIX realistic(v7)` · `ip-adapter-faceid_sd15_lora.saf…` (LoRA) · `ip-adapter-faceid_sd15` (IPA) _(+5)_ |
| 第二好用兼容SD1.5和XL_高清_修复_lora_CN | ControlNet 深度图引导生成、＋面部细节增强、＋UltimateSD 放大 | `majicMIX realistic_v7` · `xl_more_art-full_v1` (LoRA) · `control_v11p_sd15_depth` (CN) _(+6)_ |
| 简单文生图_4K超清 | UltimateSD 高清放大 | `墨幽︱2.5D(v2)` · `Keqing | Genshin Impact | 3in1 …` (LoRA) · `4x-UltraSharp` (Up) |
| 简单的Logo动画2.0 | 视频帧插值补帧、ControlNet Tile 高清重绘、＋超分放大 | `dreamshaper_8` · `lcm-lora-sdv1-5` (LoRA) · `control_v11f1e_sd15_tile` (CN) _(+5)_ |
| 简易主题摄影 | IPAdapter+ 增强风格参考、ControlNet 姿态控制生成、＋超分放大 | `TWing Shadow光影摄影(v2.0)` · `ip-adapter-plus_sd15` (IPA) · `control_v11p_sd15_openpose` (CN) _(+2)_ |
| 精准控图 | IPAdapter 人脸参考生成、＋面部细节增强、＋UltimateSD 放大 | `ip-adapter-plus-face_sd15` (IPA) · `8x_NMKD-Superscale_150000_G` (Up) _(+4)_ |
| 线稿上色_图像放大 | 线稿/草图转彩色图像、ControlNet 线稿引导生成、＋超分放大 | `control_v11p_sd15s2_lineart_anime` (CN) · `RealESRGAN_x4plus` (Up) _(+1)_ |
| 终极创意工作流程 | 综合创意特效图像生成、＋超分放大 | `turbovisionxlSuperFastXLBasedOn…` · `4x-UltraSharp` (Up) |
| 老照片修复 | ControlNet Tile 高清重绘、＋超分放大 | `2558_4095_4814` · `control-lora-recolor-rank256` (CN) · `ESRGAN_4x` (Up) _(+3)_ |
| 老照片修复-面部修复上色版 | ControlNet Tile 高清重绘、＋超分放大 | `2558_4095_4814` · `control-lora-recolor-rank256` (CN) · `ESRGAN_4x` (Up) _(+3)_ |
| 肖像重绘放大器 | ControlNet 软边缘引导生成、＋UltimateSD 放大 | `realisticVisionV51_v51VAE` · `control_hed-fp16` (CN) · `1x_DeBLR` (Up) _(+3)_ |
| 背景融合产品 | IPAdapter+ 增强风格参考、ControlNet 深度图引导生成、＋UltimateSD 放大 | `revAnimated_v122.safetensors(re…` · `ip-adapter-plus_sd15` (IPA) · `control_v11f1p_sd15_depth` (CN) _(+2)_ |
| 自动化壁纸生成器 | 创意壁纸图像生成、＋超分放大 | `DreamShaper XL_Turbo DPMpp SDE(…` · `BSRGANx2` (Up) _(+1)_ |
| 艺术二维码 | 艺术二维码生成、ControlNet QR码特效、＋UltimateSD 放大 | `2576_4113_4833` · `control_v1p_sd15_qrcode_monster` (CN) · `4x-UltraSharp` (Up) |
| 艺术二维码生成器 | 艺术二维码生成、ControlNet QR码特效、＋面部细节增强 | `end_v10` · `qrCodeMonster_v20` (CN) · `4x-UltraSharp` (Up) _(+2)_ |
| 视频反向插帧 | 局部区域重绘 (Inpaint)、输出为视频格式 | `epicrealism_v10-inpainting` |
| 视频提升分辨率 | IPAdapter+ 增强风格参考、ControlNet Tile 高清重绘、＋超分放大 | `0001softrealistic_v154xxx` · `15lcm` (LoRA) · `ip-adapter-plus_sd15` (IPA) _(+11)_ |
| 调整画面的整体颜色 | ControlNet Tile 高清重绘、＋面部细节增强、＋超分放大 | `dreamshaper_8` · `GoodHands-beta2` (LoRA) · `control_v11f1e_sd15_tile` (CN) _(+4)_ |
| 超写实风格摄影优化器 | ControlNet Tile 高清重绘、＋面部细节增强 | `foddaxlPhotorealism_v60` · `OpenPoseXL2` (CN) · `RealESRGAN_x4plus` (Up) _(+5)_ |
| 迪士尼换脸 | 人脸替换/换脸、ControlNet 姿态控制生成、＋面部细节增强 | `control_v11p_sd15_openpose_fp16` (CN) · `4x-UltraSharp` (Up) _(+3)_ |
| 重绘工作流 | 局部区域重绘 (Inpaint) | `dreamshaper_8` _(+1)_ |
| 面部服饰融合 | IPAdapter FaceID 人脸一致性生成、ControlNet 引导图像生成、＋面部细节增强 | `majicMIX realistic(v7)` · `ip-adapter-faceid-plusv2_sd15` (IPA) · `ESRGAN_4x` (Up) _(+5)_ |
| 高清修复 | ControlNet Tile 高清重绘 | `DreamShaper XL_Turbo DPMpp SDE(…` · `Twe(v1)` (LoRA) · `control_v11f1e_sd15_tile` (CN) _(+4)_ |
| 高清放大 | CCSR 超分辨率放大 | `real-world_ccsr` (Up) |
| 高清放大UltimateUpscale | ControlNet Tile 高清重绘 | `revAnimated_v121` · `control_v11f1e_sd15_tile` (CN) · `RealESRGAN_x4plus` (Up) |
| 魔法画布实时绘画 | 实时草图/绘画生成、ControlNet 姿态控制生成、＋面部细节增强 | `epicrealism_naturalSin` · `control_v11p_sd15_openpose_fp16` (CN) · `4x-UltraSharp` (Up) _(+2)_ |
| 龙年人脸转绘 | IPAdapter FaceID 人脸一致性生成、＋面部细节增强、＋UltimateSD 放大 | `bluePencilXL_v200(bluePencilXL_…` · `ip-adapter-faceid_sdxl` (IPA) · `4x-UltraSharp` (Up) _(+4)_ |

## 🎲 AI 2D→3D（4 个）

| 工作流文件 | 作用描述 | 主要模型 |
|-----------|---------|---------|
| 一张图片转化3D多视角图 | Zero123 多角度三维视图 | `stable_zero123` |
| 图像转3D效果_SV3D | SV3D 三维旋转视图、输出为视频格式 | `IP DESIGN _ 3D可爱化模型_V3.1` _(+3)_ |
| 手绘到3d模型 | TripoSR 图像转 3D 网格、ControlNet Tile 高清重绘 | `anything-v5-PrtRE` · `control_lora_rank128_v11f1e_sd1…` (CN) |
| 生成三视图 | Zero123 多角度三维视图 | `stable_zero123` |

## 🏠 AI室内设计（4 个）

| 工作流文件 | 作用描述 | 主要模型 |
|-----------|---------|---------|
| AI室内设计 | 室内/建筑效果图生成、ControlNet 深度图引导生成 | `Realistic Vision V6.0 B1 真实视觉 R…` · `Add More Details - Detail Enhan…` (LoRA) · `control_v11f1p_sd15_depth` (CN) _(+1)_ |
| 字节跳动Hyper-SDXL-室内效果图-多种CN控制 | IPAdapter+ 增强风格参考、ControlNet 深度图引导生成 | `AiARTiST-HyperRAY XL 室内设计渲染系统 X…` · `2-新版-通用-禅意&侘寂&奢华别墅_XL_壹(V1.0)` (LoRA) · `ip-adapter-plus_sdxl_vit-h` (IPA) _(+7)_ |
| 室内设计工作流 | 室内/建筑效果图生成、ControlNet 深度图引导生成 | `MOHAWK(v1.8(VAE_Baked))` · `新版专用LORA-LCM-基础模型升级版(V1.0)` (LoRA) · `sai_xl_depth_256lora` (CN) _(+1)_ |
| 毛坯房-参考出室内效果图 | IPAdapter+ 增强风格参考、ControlNet 深度图引导生成 | `majicMIX realistic(v7)` · `原木奶油风(V0.1)` (LoRA) · `ip-adapter-plus_sd15` (IPA) _(+5)_ |

## 📷 AI摄影写真（3 个）

| 工作流文件 | 作用描述 | 主要模型 |
|-----------|---------|---------|
| 产品摄影 | IPAdapter+ 增强风格参考、ControlNet 深度图引导生成 | `juggernautXL_v7Rundiffusion` · `ip-adapter-plus_sd15` (IPA) · `control-lora-canny-rank256` (CN) _(+3)_ |
| 人像写真 | IPAdapter FaceID 人脸一致性生成、ControlNet Tile 高清重绘、＋面部细节增强 | `ip-adapter-faceid-plusv2_sd15_l…` (LoRA) · `ip-adapter-faceid-plusv2_sd15` (IPA) · `control_v11f1e_sd15_tile` (CN) _(+6)_ |
| 人像写真-IPAdapter版 | IPAdapter FaceID 人脸一致性生成、ControlNet Tile 高清重绘、＋面部细节增强 | `ip-adapter-faceid-plusv2_sd15_l…` (LoRA) · `ip-adapter-faceid-plusv2_sd15` (IPA) · `control_v11f1e_sd15_tile` (CN) _(+6)_ |

## ✍️ AI文字艺术（8 个）

| 工作流文件 | 作用描述 | 主要模型 |
|-----------|---------|---------|
| AI_LOGO生成 | 文字/Logo 艺术生成 | `crystalClearXL_ccxl` · `Harrlogos_v2.0` (LoRA) |
| 在任何物体上放置文字 | 文字/Logo 艺术生成 | `RealitiesEdgeXL_` · `Harrlogos_v2.0` (LoRA) |
| 文字logo生图 | ControlNet Canny 边缘引导 | `墨幽︱二次元(v2)` · `control_v11p_sd15_canny` (CN) |
| 文字头像 | ControlNet Canny 边缘引导 | `revAnimated_v122(V1.0)` · `字体龙(V1.0)` (LoRA) · `control_v11p_sd15_canny` (CN) |
| 文字特效 | IPAdapter+ 增强风格参考、ControlNet Tile 高清重绘 | `majicMIX realistic(v7)` · `ip-adapter-plus_sd15` (IPA) · `control_v11f1e_sd15_tile` (CN) _(+4)_ |
| 艺术字 | ControlNet 深度图引导生成 | `ReV Animated(v1.2.2)` · `control_v11f1p_sd15_depth` (CN) _(+1)_ |
| 艺术字_clip视觉合成 | IPAdapter 图像风格参考、ControlNet Canny 边缘引导 | `majicMIX realistic(v2威力加强定制版)` · `ip-adapter_sd15` (IPA) · `control_v11p_sd15_canny` (CN) _(+1)_ |
| 轻松创作艺术字 | IPAdapter+ 增强风格参考 | `ip-adapter-plus_sdxl_vit-h` (IPA) _(+2)_ |

## ✏️ AI线稿绘画（5 个）

| 工作流文件 | 作用描述 | 主要模型 |
|-----------|---------|---------|
| 一键转手绘 | 线稿/草图转彩色图像 | — |
| 基于SDXL实现的线稿生成器 | ControlNet 引导图像生成 | `t2i-adapter_diffusers_xl_sketch` (CN) |
| 线稿上色 | 线稿/草图转彩色图像 | `control_v11p_sd15_lineart_fp16` (CN) |
| 线稿转图 | 线稿/草图转彩色图像、ControlNet 线稿引导生成 | `DreamShaper(8)` · `control_v11p_sd15_lineart` (CN) _(+1)_ |
| 草稿生成线稿 | 线稿/草图辅助生成 | `sargezt_xl_softedge` (CN) |

## 🎨 AI创意趣玩（137 个）

| 工作流文件 | 作用描述 | 主要模型 |
|-----------|---------|---------|
| Cute_you_By_Rui | IPAdapter 人脸参考生成、ControlNet 姿态控制生成 | `3254_4924_5753` · `3248_4906_5737` (LoRA) · `ip-adapter-plus-face_sdxl_vit-h` (IPA) _(+4)_ |
| IC-Light_All-In-One | IC-Light 光影重打光 | `majicMIX realistic(v7)` |
| IPAdapter_basic_SDXL | IPAdapter 图像风格参考 | `sd_xl_base_1.0` · `ip-adapter_sdxl` (IPA) _(+2)_ |
| IPAdapter_canny | IPAdapter+ 增强风格参考、ControlNet Canny 边缘引导 | `dreamshaper_8` · `ip-adapter-plus_sd15` (IPA) · `control_v11p_sd15_canny_fp16` (CN) _(+2)_ |
| IPAdapter_img_variations | IPAdapter 图像风格参考 | `dreamshaper_8` · `ip-adapter_sd15` (IPA) _(+2)_ |
| IPAdapter人脸迁移工作流_新手向 | IPAdapter FaceID 人脸一致性生成、ControlNet 姿态控制生成、＋面部细节增强 | `majicMIX realistic éº¦æ©åå®_v7` · `ip-adapter-faceid-plusv2_sd15_lora` (LoRA) · `ip-adapter-faceid-plusv2_sd15` (IPA) _(+4)_ |
| IPAdaptor_Face_ID | IPAdapter FaceID 人脸一致性生成、ControlNet 姿态控制生成、＋面部细节增强 | `ip-adapter-faceid-plusv2_sd15_lora` (LoRA) · `ip-adapter-faceid-plusv2_sd15` (IPA) · `control_v11p_sd15_openpose_fp16` (CN) _(+4)_ |
| Instant_Design_实时设计 | 实时图像设计工具 | — |
| PS实时绘图 | ControlNet Canny 边缘引导 | `ReVAnimated_v122_V122` · `X光透视建筑艺术_v1.0` (LoRA) · `control_canny-fp16` (CN) |
| Playground2.5文生图 | Playground V2.5 图像生成 | `Playground(v2.5)` |
| SD1.5修复老照片 | IC-Light/Recolor 光影重打光 | `majicMIX realistic(v7)` · `现代轻奢住宅_FX-Design` (LoRA) · `ioclab_sd15_recolor` (CN) _(+3)_ |
| SD1.5模型深度图简易工作流_图生图 | ControlNet 线稿引导生成 | `Depth深度图1.5_1.0` · `Depth_XL深度图_1.0` (LoRA) · `control_v11p_sd15_lineart_fp16` (CN) |
| SDXL文生图 | SD 文生图（文字转图像） | `基础模型_XL_v1.0(base1.0)` _(+1)_ |
| Snap_IDPhoto_证件照 | 证件照自动生成、IPAdapter FaceID 人脸一致性生成、＋面部细节增强 | `majicmixRealistic_v7` · `ip-adapter-faceid-plusv2_sd15_lora` (LoRA) · `ip-adapter-faceid-plusv2_sd15` (IPA) _(+6)_ |
| XY_表_工作流 | XY 参数对比工作流 | `majicMIX realistic(v7)` · `户外写真丨纯白冬日恋歌(V1.0)` (LoRA) |
| blank_token | 提示词/嵌入词技巧示例 | `v1-5-pruned-emaonly` _(+1)_ |
| canny | ControlNet Canny 边缘引导 | `absolutereality_v181` · `control_v11p_sd15_canny_fp16` (CN) _(+1)_ |
| cascade文生图工作刘 | SD 文生图（文字转图像） | — _(+1)_ |
| comfuUI_双人 | IPAdapter 人脸参考生成 | `3254_4924_5753` · `3248_4906_5737` (LoRA) · `ip-adapter-plus-face_sdxl_vit-h` (IPA) _(+5)_ |
| comfyui_文生图_SDXL标准工作流 | SD 文生图（文字转图像） | `Stable Diffusion SDXL refiner_1…` _(+1)_ |
| controlnet串联参考 | ControlNet 姿态控制生成 | `nightSkyYOZORAStyle_yozoraV1Origin` · `yaeMikoRealistic_yaemikoMixed` (LoRA) · `control_v11f1p_sd15_depth` (CN) _(+1)_ |
| denoise_impact_on_latent | 潜空间放大/降噪示例 | `v1-5-pruned-emaonly` _(+1)_ |
| depth | ControlNet 深度图引导生成 | `dreamshaper_8` · `t2iadapter_zoedepth_sd15v1` (CN) _(+1)_ |
| faceID换脸 | 人脸替换/换脸、IPAdapter FaceID 人脸一致性生成 | `majicMIX realistic(v7)` · `ip-adapter-faceid-plusv2_sd15_l…` (LoRA) · `ip-adapter-faceid-plusv2_sd15` (IPA) _(+1)_ |
| horrors_negative | 提示词/嵌入词技巧示例 | `v1-5-pruned-emaonly` _(+1)_ |
| img2img_SDXL | SD 图生图（img2img） | `sd_xl_base_1.0` _(+1)_ |
| ip-adapter_controlnet-workflow | IPAdapter+ 增强风格参考、ControlNet Canny 边缘引导 | `majicmixRealistic_betterV2V25` · `ip-adapter-plus_sd15` (IPA) · `control_v11p_sd15_canny` (CN) _(+2)_ |
| ip-adapter_workflow | IPAdapter+ 增强风格参考 | `nightSkyYOZORAStyle_yozoraV1Origin` · `ip-adapter-plus_sd15` (IPA) _(+1)_ |
| ip-adapter_混合蒙版工作流 | ControlNet 姿态控制生成 | `CounterfeitV25_25` · `control_v11f1p_sd15_depth` (CN) _(+3)_ |
| lcm_绘画工作流 | LCM 高速实时图像生成 | `realisticVisionV51_v51VAE` · `lcm_sd1.5_pytorch_lora_weights` (LoRA) _(+1)_ |
| lora串联参考 | 多 LoRA 叠加示例 | `v1-5-pruned-emaonly` · `7thMarchHSRv2` (LoRA) |
| may-remini粘土卡通版-粘土粘土clay | ControlNet 引导图像生成 | `art universe(V2.0)` · `PLUS (high strength)` (IPA) · `control-lora-sketch-rank256` (CN) |
| may-remini粘土美颜版-粘土粘土clay | ControlNet Tile 高清重绘 | `art universe(V2.0)` · `PLUS (high strength)` (IPA) · `TTPLANET_Controlnet_Tile_realis…` (CN) |
| multiple_controlnets | ControlNet 姿态控制生成 | `absolutereality_v181` · `control_v11e_sd15_shuffle` (CN) _(+2)_ |
| pose | ControlNet 姿态控制生成 | `dreamshaper_8` · `control_v11p_sd15_openpose_fp16` (CN) _(+1)_ |
| revision_SDXL | SDXL 文生图/图生图工作流 | `sd_xl_base_1.0` _(+2)_ |
| timestepping | Conditioning 高级控制示例 | `sd_xl_base_1.0` _(+1)_ |
| timestepping_style_model | Conditioning 高级控制示例 | `v1-5-pruned-emaonly` _(+2)_ |
| upscale_tile_controlnet | ControlNet Tile 高清重绘 | `v1-5-pruned-emaonly` · `control_v11f1e_sd15_tile` (CN) _(+1)_ |
| word_weighting | 提示词/嵌入词技巧示例 | `v1-5-pruned-emaonly` _(+1)_ |
| 一句话AI生图 | SD 文生图（文字转图像） | `1540_2949_3459` · `2415_3945_4641` (LoRA) _(+1)_ |
| 一键3D漫画头像 | IPAdapter 人脸参考生成 | `2459_3990_4692` · `ip-adapter-plus-face_sd15` (IPA) _(+1)_ |
| 一键换衣 | 虚拟换装、IPAdapter 图像风格参考 | `majicMIX realistic(v5)` · `Twe(v1)` (LoRA) · `ip-adapter_sd15` (IPA) _(+2)_ |
| 一键生成3d头像 | IPAdapter+ 增强风格参考、＋面部细节增强 | `RealCartoon-Pixar(V8)` · `ip-adapter-plus_sd15` (IPA) · `4x-UltraSharp` (Up) _(+3)_ |
| 一键生成多张图片 | 批量多图生成 | `1540_2949_3459` · `2415_3945_4641` (LoRA) _(+1)_ |
| 上妆 | AI 美妆/上妆效果生成、＋面部细节增强 | `Realistic Vision V6.0 B1 真实视觉 R…` _(+2)_ |
| 为图片赋诗一首 | 文字图像叠加合成 | — |
| 乐高世界 | 卡通/风格化图像生成 | `2507_4041_4747` · `2750_4290_5037` (LoRA) _(+1)_ |
| 二次元转真实_换脸_修脸_放大 | 人脸替换/换脸、IPAdapter FaceID 人脸一致性生成、＋面部细节增强 | `majicMIX realistic(v7)` · `Miao girl costume(v1.0)` (LoRA) · `ip-adapter-faceid-plusv2_sd15` (IPA) _(+6)_ |
| 产品外包装生成器 | IPAdapter+ 增强风格参考、ControlNet 深度图引导生成 | `399_1018_1286` · `ip-adapter-plus_sd15` (IPA) · `control_v11f1p_sd15_depth` (CN) _(+2)_ |
| 产品设计 | ControlNet Inpaint 精准重绘 | `productDesign_eddiemauro20` · `control_v11p_sd15_inpaint` (CN) |
| 人人能上手的DIY壁纸工作流_一键版 | 创意壁纸图像生成 | `Playground(v2.5)` |
| 人像大师 | PortraitMaster 人像精修生成、ControlNet 引导图像生成 | `RealVisXL V2.0(V2.0 (BakedVAE))` |
| 像素图像生成器 | 像素风格图像生成 | `683_3660_4305` |
| 像素级放大工作流 | 图像放大/超分辨率示例 | `dreamshaper_8` _(+1)_ |
| 光影字_换脸_修脸_放大 | 人脸替换/换脸、IPAdapter FaceID 人脸一致性生成、＋面部细节增强 | `majicMIX realistic(v7)` · `Miao girl costume(v1.0)` (LoRA) · `ip-adapter-faceid-plusv2_sd15` (IPA) _(+6)_ |
| 具有自定义保存文件夹的ControlNet_Passes提取器 | ControlNet 预处理图批量提取 | — |
| 写实人物转漫画 | 图像转漫画/动漫风格 | `683_3660_4305` |
| 初学者工作流_A1111_风格_高分辨率提升_面部细节增强 | 扩散模型图像生成、＋面部细节增强 | `DucHaiten-AIart-基础模型升级版(V1.0)` _(+4)_ |
| 利用clipseg自动更换人物背景 | 人物背景替换、IPAdapter 图像风格参考、＋面部细节增强 | `deliberate_v3` · `ip-adapter_sd15` (IPA) · `control_v11p_sd15_openpose` (CN) _(+3)_ |
| 动漫角色转真人 | ControlNet Canny 边缘引导、＋面部细节增强 | `majicMIX realistic(v7)` · `Miao girl costume(v1.0)` (LoRA) · `control_v11p_sd15_canny` (CN) _(+4)_ |
| 动漫转真实_换脸_修脸_放大 | 人脸替换/换脸、IPAdapter FaceID 人脸一致性生成、＋面部细节增强 | `majicMIX realistic(v7)` · `Miao girl costume(v1.0)` (LoRA) · `ip-adapter-faceid-plusv2_sd15` (IPA) _(+6)_ |
| 动画Gif_-_从一幅图像到另一幅图像 | ControlNet Tile 高清重绘 | `juggernaut_final` · `control_v11f1e_sd15_tile` (CN) |
| 卡通 | IPAdapter FaceID 人脸一致性生成 | `bluePencilXL_v200(bluePencilXL_…` · `ip-adapter-faceid_sdxl` (IPA) _(+1)_ |
| 卡通合影HoldMyHand_._Rui | IPAdapter 人脸参考生成 | `3254_4924_5753` · `3248_4906_5737` (LoRA) · `ip-adapter-plus-face_sdxl_vit-h` (IPA) _(+4)_ |
| 卡通图像 | IPAdapter 人脸参考生成、ControlNet 姿态控制生成 | `3254_4924_5753` · `3248_4906_5737` (LoRA) · `ip-adapter-plus-face_sdxl_vit-h` (IPA) _(+4)_ |
| 卡通头像 | IPAdapter 人脸参考生成 | `revAnimated_v11(v11)` · `ip-adapter-plus-face_sd15` (IPA) _(+1)_ |
| 卡通头像生成 | IPAdapter 人脸参考生成 | `2459_3990_4692` · `ip-adapter-plus-face_sd15` (IPA) _(+1)_ |
| 古风山水姓氏头像 | ControlNet QR码特效、＋面部细节增强 | `revAnimated_v122(V1.0)` · `lora3(2.0)` (LoRA) · `control_v1p_sd15_qrcode_monster` (CN) _(+2)_ |
| 同风格图片批量生成 | StyleAligned 多图同风格批量 | `sdXL_v10VAEFix` |
| 图片扩展 | ControlNet Inpaint 精准重绘 | `371_928_1178` · `control_v11p_sd15_inpaint` (CN) _(+1)_ |
| 图片扩展工作流 | IPAdapter+ 增强风格参考、ControlNet Inpaint 精准重绘 | `XXMix_9realistic基础模型升级版(v1.0)` · `ip-adapter-plus_sd15` (IPA) · `control_v11p_sd15_inpaint` (CN) _(+1)_ |
| 图片转绘V1.1 | ControlNet Canny 边缘引导 | `2634_4172_4897` · `sai_xl_canny_256lora` (CN) |
| 图片风格替换工作流 | ControlNet Canny 边缘引导 | `majicMIX realistic(v7)` · `control_v11e_sd15_shuffle` (CN) _(+1)_ |
| 图生图_高度接近 | ControlNet 线稿引导生成 | `majicMIX realistic(v7)` · `control_v11p_sd15_lineart` (CN) |
| 基因融合器 | IPAdapter 人脸参考生成 | `realisticStockPhoto_v10` · `ip-adapter-plus-face_sdxl_vit-h` (IPA) _(+1)_ |
| 基本的SD_1.5_Img2img工作流 | SD 图生图（img2img） | `dreamshaper_8` |
| 大头Q版图像生成器 | Q版/大头卡通形象生成、IPAdapter 图像风格参考 | `againmixchibi_V1(1.0)` |
| 姓名字3D墙半成品 | ControlNet Canny 边缘引导、＋面部细节增强 | `ReV Animated(v1.2.2-EOL)` · `3d wallpaper-balloon(v1)` (LoRA) · `control_v11p_sd15_canny` (CN) _(+2)_ |
| 姓氏头像之国风汉服 | ControlNet QR码特效、＋面部细节增强 | `niji-动漫二次元(v1.0)` · `国风露肩汉服(v1.0)` (LoRA) · `control_v1p_sd15_qrcode_monster` (CN) _(+3)_ |
| 姓氏头像之性感风 | ControlNet Inpaint 精准重绘、＋面部细节增强 | `XXMix_9realistic_4.0(4.0)` · `hanfu 汉服(v3.0)` (LoRA) · `control_v11p_sd15_inpaint` (CN) _(+2)_ |
| 姓氏头像之风景2 | ControlNet QR码特效、＋面部细节增强 | `revAnimated_v122(V1.0)` · `龙与少年，江南飞花(1.0)` (LoRA) · `control_v1p_sd15_qrcode_monster` (CN) _(+2)_ |
| 姓氏头像可爱卡通女 | ControlNet Inpaint 精准重绘、＋面部细节增强 | `ReV Animated(v1.2.2)` · `国风萌玩(V1.0)` (LoRA) · `control_v11p_sd15_inpaint` (CN) _(+2)_ |
| 姓氏头像可爱卡通男 | ControlNet Inpaint 精准重绘、＋面部细节增强 | `ReV Animated(v1.2.2)` · `国风萌玩 | Chinese style cute doll(…` (LoRA) · `control_v11p_sd15_inpaint` (CN) _(+2)_ |
| 定制万能卡通形象只需一张真人头像_一张姿势图 | IPAdapter 人脸参考生成、ControlNet 姿态控制生成 | `3254_4924_5753` · `3248_4906_5737` (LoRA) · `ip-adapter-plus-face_sdxl_vit-h` (IPA) _(+4)_ |
| 实时模糊变清晰_LCM_Controln | ControlNet Tile 高清重绘 | `majicMIX realistic(v7)` · `LCM-LoRA for基础模型1.5(v1.0)` (LoRA) · `coadapter-depth-sd15v1` (CN) _(+1)_ |
| 实时绘画 | 实时草图/绘画生成、IPAdapter 图像风格参考 | `Deliberate_v2` · `LCM_LoRA_SDv15` (LoRA) · `ip-adapter_sd15` (IPA) _(+2)_ |
| 实时绘画-可以直接使用 | 实时草图/绘画生成、ControlNet Tile 高清重绘 | `墨幽人造人(v1080-none)` · `Twe(v1)` (LoRA) · `control_v11f1e_sd15_tile` (CN) _(+1)_ |
| 实时绘画工作流 | 实时草图/绘画生成、ControlNet 深度图引导生成 | `3dAnimationDiffusion_v10` · `LCM-LoRA_sd15` (LoRA) · `control_sd15_depth_anything_fp16` (CN) _(+5)_ |
| 小说推文_视频反推生图 | IPAdapter 人脸参考生成 | `683_3660_4305` · `ip-adapter-plus-face_sd15` (IPA) _(+1)_ |
| 情侣合影工作流_You_Me_._Rui | IPAdapter 人脸参考生成 | `3254_4924_5753` · `3248_4906_5737` (LoRA) · `ip-adapter-plus-face_sdxl_vit-h` (IPA) _(+5)_ |
| 手办生成器 | IPAdapter 人脸参考生成、ControlNet 姿态控制生成 | `3254_4924_5753` · `3248_4906_5737` (LoRA) · `ip-adapter-plus-face_sdxl_vit-h` (IPA) _(+4)_ |
| 扩图 | 图像外扩 (Outpainting)、ControlNet Inpaint 精准重绘 | `Realistic Vision V6.0 B1 真实视觉 R…` · `control_v11p_sd15_inpaint` (CN) |
| 扩图工作流 | 图像外扩 (Outpainting)、IPAdapter+ 增强风格参考 | `dvarchMultiPrompt_dvarchExterior` · `ip-adapter-plus_sd15` (IPA) · `control_v11p_sd15_inpaint` (CN) _(+1)_ |
| 扩展图片_无需提示 | IPAdapter 图像风格参考、ControlNet Inpaint 精准重绘 | `realisticVisionV60B1_v60B1VAE` · `ip-adapter_sd15` (IPA) · `control_v11p_sd15_inpaint` (CN) _(+2)_ |
| 抠图蒙版_clip合成 | IPAdapter 图像风格参考 | `DgirlV2.1-真实质感强化(V3.0)` · `ip-adapter_sd15` (IPA) _(+1)_ |
| 拜年卡通头像工作流 | IPAdapter 人脸参考生成、ControlNet 姿态控制生成 | `Samaritan 3d Cartoon(V4.0)` · `Concept Sliders: cartoon卡通化(V1.0)` (LoRA) · `ip-adapter-plus-face_sdxl_vit-h` (IPA) _(+6)_ |
| 换脸工作流-SAM分割版 | 人脸替换/换脸、＋面部细节增强 | `majicMIX realistic(v7)` · `LEOSAM's FilmGirl 胶片风 Film Grai…` (LoRA) _(+2)_ |
| 文生图_换脸 | 人脸替换/换脸、IPAdapter FaceID 人脸一致性生成、＋面部细节增强 | `majicMIX realistic(v7)` · `Miao girl costume(v1.0)` (LoRA) · `ip-adapter-faceid-plusv2_sd15` (IPA) _(+5)_ |
| 文生图标准工作流 | ControlNet 姿态控制生成 | `nightSkyYOZORAStyle_yozoraV1Origin` · `yaeMikoRealistic_yaemikoMixed` (LoRA) · `control_v11p_sd15_openpose` (CN) _(+1)_ |
| 更换服装模特电商领域落地应用工作流 | ControlNet 姿态控制生成、＋面部细节增强 | `epicphotogasm_x` · `control_v11p_sd15_lineart` (CN) _(+4)_ |
| 最终ip-adapter_缩放模块 | IPAdapter+ 增强风格参考、ControlNet Tile 高清重绘 | `dvarchMultiPrompt_dvarchExterior` · `ip-adapter-plus_sd15` (IPA) · `control_v11f1e_sd15_tile` (CN) _(+4)_ |
| 梦幻风格海报 | ControlNet Canny 边缘引导 | `ReVAnimated_v122_V122(V1.22)` · `control_v11p_sd15_canny` (CN) _(+1)_ |
| 深度图生成图片_最小闭环工作流 | ControlNet 深度图引导生成 | `sd_xl_base_1.0` · `control_v11f1p_sd15_depth` (CN) |
| 混合图像生成结果 | IPAdapter 图像风格参考 | `epicphotogasm_v1` · `ip-adapter_sd15` (IPA) _(+2)_ |
| 漫画制作器 | ControlNet Canny 边缘引导 | `⋅ ⊣ Realities Edge XL ⊢ ⋅ LCM+基…` · `control-lora-canny-rank256` (CN) |
| 漫画连环画 | 漫画分格/图像网格排版 | `starlightXLAnimated_v3` _(+1)_ |
| 照片动漫风格化 | WD14 自动标注图像 | `Cetus-Mix(CetusMix_WhaleFall2)` _(+1)_ |
| 照片转3D卡通头像 | IPAdapter+ 增强风格参考、＋面部细节增强 | `RealCartoon-Pixar(V8)` · `ip-adapter-plus_sd15` (IPA) · `4x-UltraSharp` (Up) _(+3)_ |
| 照片转素描 | ControlNet 引导图像生成 | `t2i-adapter_diffusers_xl_sketch` (CN) |
| 照片风格化disney2.5d | IPAdapter+ 增强风格参考、ControlNet 姿态控制生成 | `迪士尼3DdisneyPixarCartoon_v10(V10)` · `LCM-LoRA for基础模型1.5(v1.0)` (LoRA) · `ip-adapter-plus_sd15` (IPA) _(+3)_ |
| 父母基因融合器 | IPAdapter 人脸参考生成 | `juggernautXL_v7Rundiffusion(V7)` · `ip-adapter-plus-face_sd15` (IPA) _(+1)_ |
| 生成动漫风 | WD14 自动标注图像 | `Cetus-Mix(CetusMix_WhaleFall2)` _(+1)_ |
| 生成提示词 | WD14 自动标注图像 | — |
| 生成无缝贴图 | 无缝贴图/纹理生成 | `基础模型_v1.5(V1.5)` |
| 电商出图-RGB蒙版 | IPAdapter+ 增强风格参考、ControlNet 深度图引导生成 | `juggernautXL_v7Rundiffusion(V7)` · `ip-adapter-plus_sd15` (IPA) · `coadapter-depth-sd15v1` (CN) _(+3)_ |
| 真人卡通化工作流 | IPAdapter 人脸参考生成、ControlNet 姿态控制生成 | `Samaritan 3d Cartoon(V4.0)` · `Concept Sliders: cartoon卡通化(V1.0)` (LoRA) · `ip-adapter-plus-face_sdxl_vit-h` (IPA) _(+4)_ |
| 真人转插画 | IPAdapter+ 增强风格参考、ControlNet Canny 边缘引导 | `3148_4802_5619` · `ip-adapter-plus_sd15` (IPA) · `control_v11p_sd15_canny` (CN) _(+2)_ |
| 真人转漫画 | 图像转漫画/动漫风格 | `683_3660_4305` |
| 简单改变风格或服装 | IPAdapter+ 增强风格参考、ControlNet Canny 边缘引导 | `majicMIX realistic(v7)` · `ip-adapter-plus_sd15` (IPA) · `control_v11p_sd15_canny` (CN) _(+1)_ |
| 简易版ComfyUI_IPA-个人ip | IPAdapter FaceID 人脸一致性生成、＋面部细节增强 | `revanimated_v122_v122` · `ip-adapter-faceid-plusv2_sd15` (IPA) _(+5)_ |
| 粘土人制作 | 粘土卡通风格转换 | `Crystal Clear XL(CCXL)` · `GFPGANv1.4` (FR) |
| 终极照片风格转换器 | IPAdapter+ 增强风格参考、ControlNet 姿态控制生成 | `sd_xl_turbo_1.0_fp16` · `ip-adapter-plus_sdxl_vit-h` (IPA) · `OpenPoseXL2` (CN) _(+1)_ |
| 脸手修复 | ComfyUI 工作流、＋面部细节增强 | `majicMIX realistic(v7)` _(+2)_ |
| 财神姓氏头相 | ControlNet QR码特效 | `3D可爱化模型(V1.0)` · `财神驾到(V1.0)` (LoRA) · `control_v1p_sd15_qrcode_monster` (CN) |
| 超级符号抽卡工作流 | ControlNet 深度图引导生成 | `ReV Animated(v1.2.2)` · `LCMTurboMix_LCM(v1.0)` (LoRA) · `control_v11f1p_sd15_depth` (CN) _(+3)_ |
| 连贯的漫画角色_可通过Controlnet_Openpose进行可动 | IPAdapter FaceID 人脸一致性生成、ControlNet 姿态控制生成 | `CHEYENNE_v14VAEBacked` · `ip-adapter-faceid-plusv2_sdxl_lora` (LoRA) · `ip-adapter-faceid-plusv2_sdxl` (IPA) _(+2)_ |
| 迷你手办 | 3D/多视角图像生成 | `MOHAWK(v1.8(VAE_Baked))` _(+1)_ |
| 速拍证件照 | 证件照自动生成、IPAdapter FaceID 人脸一致性生成、＋面部细节增强 | `majicMIX realistic(v7)` · `ip-adapter-faceid_sd15_lora.saf…` (LoRA) · `ip-adapter-faceid-plusv2_sd15` (IPA) _(+7)_ |
| 静态红包封面一键生成 | 节日动态封面生成 | `TurboVisionXL(V4.3.1)` · `Enhancer(xl_more_art-full-v1)` (LoRA) |
| 面部表情控制 | 多表情/情绪矩阵批量生成 | `realisticVisionV51_v51VAE` |
| 风格化文本生成 | ControlNet 深度图引导生成 | `juggernautXL_v7Rundiffusion` · `Harrlogos_v2.0` (LoRA) · `control-lora-canny-rank128` (CN) _(+1)_ |
| 风格转绘动漫风格 | IPAdapter+ 增强风格参考、ControlNet Canny 边缘引导 | `3148_4802_5619` · `ip-adapter-plus_sd15` (IPA) · `control_v11p_sd15_canny` (CN) _(+2)_ |
| 驯服_提示词-ELLA工作流 | ELLA 增强文本理解工作流 | `Realistic Vision V6.0 B1 真实视觉 R…` |
| 鲜花光影工作流 | IPAdapter FaceID 人脸一致性生成、IC-Light/Recolor 光影重打光、＋面部细节增强 | `majicMIX realistic(v7)` · `Miao girl costume(v1.0)` (LoRA) · `ip-adapter-faceid-plusv2_sd15` (IPA) _(+6)_ |
| 龙头像生成工作流 | ControlNet QR码特效、＋面部细节增强 | `XXMix_9realistic_4.0(4.0)` · `真实龙(1.0)` (LoRA) · `control_v1p_sd15_qrcode_monster` (CN) _(+5)_ |
| 龙男姓氏头像工作流 | ControlNet QR码特效、＋面部细节增强 | `XXMix_9realistic_4.0(4.0)` · `真实龙(1.0)` (LoRA) · `control_v1p_sd15_qrcode_monster` (CN) _(+5)_ |

## 📖 入门基础（39 个）

| 工作流文件 | 作用描述 | 主要模型 |
|-----------|---------|---------|
| SDXL_Refiner | SDXL 文生图/图生图工作流 | `sd_xl_base_1.0_0.9vae` _(+2)_ |
| SDXL_advanced | SDXL 文生图/图生图工作流 | `sd_xl_base_1.0` _(+2)_ |
| SDXL_base_only | SDXL 文生图/图生图工作流 | `sd_xl_base_1.0` _(+1)_ |
| SDXL_simple | SDXL 文生图/图生图工作流 | `sd_xl_base_1.0` _(+1)_ |
| SDXL_text_g-l | SDXL 文生图/图生图工作流 | `sd_xl_base_1.0` _(+2)_ |
| area_vs_gligen | 区域/条件控制图像生成 | `dreamshaper_8` _(+1)_ |
| basic_latent_batch | ComfyUI 基础文生图（入门示例） | `v1-5-pruned-emaonly` _(+1)_ |
| basic_lora | ComfyUI 基础文生图（入门示例） | `dreamshaper_8Inpainting` · `ghibli_style_offset` (LoRA) _(+1)_ |
| basic_parametrized | ComfyUI 基础文生图（入门示例） | `v1-5-pruned-emaonly` _(+1)_ |
| basic_workflow | ComfyUI 基础文生图（入门示例） | `v1-5-pruned-emaonly` |
| basic_workflow_ext_vae | ComfyUI 基础文生图（入门示例） | `v1-5-pruned-emaonly` _(+1)_ |
| clip_skip | 提示词/嵌入词技巧示例 | `v1-5-pruned-emaonly` _(+1)_ |
| compare_checkpoints | 效果对比工作流 | `absolutereality_v181` _(+2)_ |
| compare_conditioning_merge | 效果对比工作流 | `realisticVisionV30_v30VAE` _(+1)_ |
| compare_samplers | 效果对比工作流 | `v1-5-pruned-emaonly` _(+1)_ |
| conditioning_area | Conditioning 高级控制示例 | `absolutereality_v181` _(+1)_ |
| conditioning_average | Conditioning 高级控制示例 | `v1-5-pruned-emaonly` _(+1)_ |
| conditioning_concat | Conditioning 高级控制示例 | `v1-5-pruned-emaonly` _(+1)_ |
| conditioning_style | Conditioning 高级控制示例 | `v1-5-pruned-emaonly` _(+2)_ |
| conditioning_unclip | Conditioning 高级控制示例 | — |
| conditioning_unclip_multiple_imgs | Conditioning 高级控制示例 | — |
| embeddings | 提示词/嵌入词技巧示例 | `v1-5-pruned-emaonly` _(+1)_ |
| gligen_box | 区域/条件控制图像生成 | `dreamshaper_8` _(+1)_ |
| multiple_loras | 多 LoRA 叠加示例 | `dreamshaper_8` · `ghibli_style_offset` (LoRA) _(+2)_ |
| save_noise_steps | 噪声步骤可视化示例 | `v1-5-pruned-emaonly` _(+1)_ |
| unclip_SDXL_refiner | SDXL 文生图/图生图工作流 | `sd_xl_refiner_1.0` _(+1)_ |
| upscale_latent | 潜空间放大/降噪示例 | `v1-5-pruned-emaonly` _(+1)_ |
| upscale_latent_SDXL | 潜空间放大/降噪示例 | `sd_xl_base_1.0` _(+2)_ |
| upscale_latent_with_model | 潜空间放大/降噪示例 | `v1-5-pruned-emaonly` _(+1)_ |
| upscale_pixel | 潜空间放大/降噪示例 | `v1-5-pruned-emaonly` _(+1)_ |
| 新手入门必看GLIGEN模型 | 区域/条件控制图像生成 | `Ink(V5[Prt-RE])` |
| 新手入门必看LCM实时生成 | ComfyUI 入门基础教程示例 | `基础模型升级版50mm f1.8 SUPER LENS(V1.0)` · `LCM-LoRA for 基础模型升级版S-D-X-L(v1.0)` (LoRA) |
| 新手入门必看SDXL-Turbo | ComfyUI 入门基础教程示例 | `基础模型升级版turbo_极速出图０等待(1.0)` |
| 新手入门必看分区生成图片 | 区域/条件控制图像生成 | `AbyssOrangeMix2 - NSFW(Mix2)` _(+2)_ |
| 新手入门必看加载LoRA | ComfyUI 入门基础教程示例 | `巧月(V1)` · `动物集-深海鲸鱼(v1)` (LoRA) |
| 新手入门必看图生图 | SD 文生图（文字转图像） | `透色光年-极氪白肖像系列大模型(v6)` |
| 新手入门必看在潜空间放大图片 | ComfyUI 入门基础教程示例 | `LEOSAM's MoonFilm 胶片风真实感大模型(Fil…` |
| 新手入门必看大模型风格融合 | ComfyUI 入门基础教程示例 | `CarDos Anime(v2.0)` _(+2)_ |
| 新手入门必看控制网络 | ControlNet 引导图像生成 | `Ink(V5[Prt-RE])` · `control_v11p_sd15_scribble` (CN) _(+1)_ |

import json
from pathlib import Path
from collections import defaultdict, Counter
from datetime import datetime

BASE = Path(__file__).resolve().parent.parent / "templates"
OUT  = Path(__file__).resolve().parent.parent / "INDEX.md"

MODEL_LOADERS = {
    'CheckpointLoaderSimple':           [(0,'ckpt')],
    'CheckpointLoader':                 [(0,'ckpt')],
    'ImageOnlyCheckpointLoader':        [(0,'ckpt')],
    'Efficient Loader':                 [(0,'ckpt')],
    'LoraLoader':                       [(0,'lora')],
    'LoraLoaderModelOnly':              [(0,'lora')],
    'Load Lora':                        [(0,'lora')],
    'LoRALoader':                       [(0,'lora')],
    'ControlNetLoader':                 [(0,'controlnet')],
    'DiffControlNetLoader':             [(0,'controlnet')],
    'ControlNetLoaderAdvanced':         [(0,'controlnet')],
    'IDControlNetLoader':               [(0,'controlnet')],
    'IPAdapterModelLoader':             [(0,'ipadapter')],
    'IPAdapterUnifiedLoader':           [(0,'ipadapter')],
    'UpscaleModelLoader':               [(0,'upscaler')],
    'CLIPVisionLoader':                 [(0,'clip_vision')],
    'VAELoader':                        [(0,'vae')],
    'UltralyticsDetectorProvider':      [(0,'detector')],
    'SAMLoader':                        [(0,'sam')],
    'SAMModelLoader (segment anything)':[(0,'sam')],
    'FaceRestoreModelLoader':           [(0,'face_restore')],
    'InstantIDModelLoader':             [(0,'instantid')],
    'PhotoMakerLoader':                 [(0,'photomaker')],
    'PhotoMakerAdapter_Loader_local':   [(0,'photomaker')],
    'PhotoMakerAdapter_Loader_fromhub': [(0,'photomaker')],
    'CCSR_Model_Select':                [(0,'upscaler')],
    'Load CheckPoint DragNUWA':         [(0,'ckpt')],
    'CR Multi-ControlNet Stack':        [(1,'controlnet')],
    'CR ControlNet Stack':              [(1,'controlnet')],
    'MagicAnimateModelLoader':          [(0,'ckpt')],
}

FUNC_MAP = [
    ('svd_img2vid_conditioning',          'SVD图生视频'),
    ('ade_animatediffloaderwithcontext',  'AnimateDiff'),
    ('ade_animatediffloader',             'AnimateDiff'),
    ('ade_applyanimatediffmodel',         'AnimateDiff'),
    ('ade_useevolvedsampling',            'AnimateDiff'),
    ('ade_animatediffloadertextmatch',    'AnimateDiff'),
    ('workflow/animate',                  'AnimateDiff'),
    ('dragnuwa run',                      'DragNUWA运动视频'),
    ('load checkpoint dragnuwa',          'DragNUWA运动视频'),
    ('magicanimate',                      'MagicAnimate动作驱动'),
    ('vhs_loadvideo',                     '视频输入'),
    ('vhs_loadvideopath',                 '视频输入'),
    ('vhs_videocombine',                  '视频输出'),
    ('rife vfi',                          '视频帧插值'),
    ('film vfi',                          '视频帧插值'),
    ('reactorfaceswap',                   'ReActor换脸'),
    ('reactor',                           'ReActor换脸'),
    ('roop',                              'Roop换脸'),
    ('idgenerationnode',                  'InstantID人像'),
    ('idbasemodelloader',                 'InstantID人像'),
    ('applyinstantid',                    'InstantID人像'),
    ('instantidfaceanalysis',             'InstantID人像'),
    ('insightfaceloader_zho',             'InstantID人像'),
    ('ipadapter_instantidloader',         'InstantID人像'),
    ('new_photomaker_generation',         'PhotoMaker换脸'),
    ('photomakeradapter_loader',          'PhotoMaker换脸'),
    ('photomakerloader',                  'PhotoMaker换脸'),
    ('zero123',                           'Zero123三维视图'),
    ('sv3d',                              'SV3D三维视图'),
    ('triposr',                           'TripoSR图转3D'),
    ('loadootdpipeline',                  'OOTDiffusion换装'),
    ('ootdgenerate',                      'OOTDiffusion换装'),
    ('supir_upscale',                     'SUPIR超分辨率'),
    ('supir_encode',                      'SUPIR超分辨率'),
    ('supir_sample',                      'SUPIR超分辨率'),
    ('ccsr_upscale',                      'CCSR超分辨率'),
    ('ultimatesdupscale',                 'UltimateSD放大'),
    ('iterativelatentupscale',            '迭代超分放大'),
    ('imageupscalewithmodel',             '模型超分放大'),
    ('facedetailer',                      'FaceDetailer'),
    ('facerestoremodelloader',            '面部修复'),
    ('segsdetailerforanimatediff',        '视频面部修复'),
    ('groundingdinosamsegment',           'SAM语义分割'),
    ('groundingdinomodelloader',          'SAM语义分割'),
    ('samdetector',                       'SAM语义分割'),
    ('samdetectorcombined',               'SAM语义分割'),
    ('image rembg',                       'RemBG去背'),
    ('image remove background',           'RemBG去背'),
    ('rembgsession',                      'RemBG去背'),
    ('layermask: birefnet',               'BiRefNet精细抠图'),
    ('birefnetultra',                     'BiRefNet精细抠图'),
    ('clipseg_',                          'CLIPSeg文字分割'),
    ('layereddiffusionapply',             'LayeredDiffusion透明背景'),
    ('layereddiffusiondecode',            'LayeredDiffusion透明背景'),
    ('inpaint_applyfooocusinpaint',       'Fooocus智能重绘'),
    ('inpaint_loadinpaintmodel',          'Fooocus智能重绘'),
    ('brushnet',                          'BrushNet笔刷重绘'),
    ('vaeencodeforinpaint',               '局部重绘Inpaint'),
    ('ipadapteradvanced',                 'IPAdapter参考'),
    ('ipadapterapply',                    'IPAdapter参考'),
    ('ipadapterfaceid',                   'IPAdapter参考'),
    ('ipadapterapplyfaceid',              'IPAdapter参考'),
    ('ipAdapterInsightFaceLoader',        'IPAdapter参考'),
    ('stylealignedbatchalign',            'StyleAligned风格对齐'),
    ('controlnetapply',                   'ControlNet引导'),
    ('controlnetapplyadvanced',           'ControlNet引导'),
    ('cr multi-controlnet stack',         'ControlNet引导'),
    ('acn_advancedcontrolnet',            'ControlNet引导'),
    ('t2i-adapter',                       'ControlNet引导'),
    ('dynamicrafterloader',               'DynamiCrafter文生视频'),
    ('dynamicrafterprocessor',            'DynamiCrafter文生视频'),
    ('acn_sparsectrlloaderadvanced',      'SparseCtrl运动控制'),
    ('acn_sparsectrlspreadmethod',        'SparseCtrl运动控制'),
    ('ic-light',                          'IC_Light'),
    ('iclight',                           'IC_Light'),
    ('portraitmaster',                    'PortraitMaster人像精修'),
    ('cr image grid',                     '漫画/图像网格排版'),
    ('cr page layout',                    '漫画/图像网格排版'),
    ('flatlatentsintosinglegrid',         '多表情/图像网格生成'),
    ('wd14tagger',                        'WD14自动标注'),
    ('clipinterrogator',                  'CLIP反推提示词'),
    ('qwenvl_api',                        'QWen-VL图文理解'),
    ('textimage',                         '文字图像叠加'),
    ('ksampler',                          '__ksampler__'),
]

FILENAME_FALLBACKS = [
    (['转漫画','漫画风','动漫风','生成动漫','漫画转绘','漫画制作','真人转插画','真人卡通','人物转漫画'], '图像转漫画/动漫风格'),
    (['动漫角色转真人','转真人','2d转真人','二次元转真实','动漫转真实'], '漫画/动漫图转真人风格'),
    (['ai写真','写真','虚拟摄影','ai摄影','aix'], '写真/摄影风格图像生成'),
    (['一件换装','换装','换衣','试装','添加服装'], '虚拟换装'),
    (['换背景','更换背景','替换背景','自动扣像','产品换背景'], '背景替换'),
    (['抠图','透明背景','移除背景','去背','透明素材'], '背景去除/抠图'),
    (['换脸','换头'], '人脸替换换脸'),
    (['超清放大','高清放大','无损放大','超分','像素级放大','高清重绘','高清化'], '图像超分/高清放大'),
    (['老照片修复','照片修复','旧照片修复'], '老照片修复与上色'),
    (['室内设计','户外设计','建筑','装修','毛坯房'], '室内/建筑设计渲染'),
    (['艺术字','文字特效','字体生成','文字logo','造字','广告词','文字','logo','放置文字'], '文字/Logo 艺术生成'),
    (['证件照'], '证件照自动生成'),
    (['二维码'], '艺术二维码生成'),
    (['姓氏头像','姓名头像'], '姓氏/主题定制头像'),
    (['头像'], '头像风格生成/转换'),
    (['海报'], '海报/宣传图生成'),
    (['产品拍摄','商品拍摄','电商产品','商业证件','商品设计'], '电商产品图生成'),
    (['图生视频','图转视频','图片转视频','静帧变视频'], 'SVD 图像转视频'),
    (['文生视频','文字生视频','文生图生视频'], '文字/图像驱动视频生成'),
    (['视频转绘','视频转视频','vid2vid'], '视频风格转绘'),
    (['视频换脸'], '视频换脸'),
    (['线稿','草稿'], '线稿/草图辅助生成'),
    (['手绘'], '图像转手绘风格'),
    (['扩图','外扩','outpainting'], '图像外扩 (Outpainting)'),
    (['局部重绘','重绘'], '局部区域重绘'),
    (['手办','盲盒','3d','三维','三视图','多视角','多视图'], '3D/多视角图像生成'),
    (['大头','q版','chibi'], 'Q版/大头卡通形象生成'),
    (['粘土','clay'], '粘土卡通风格转换'),
    (['卡通','乐高','皮克斯','迪士尼'], '卡通/风格化图像生成'),
    (['无缝贴图','贴图纹理','纹理生成'], '无缝贴图/纹理生成'),
    (['壁纸','diy'], '创意图像/壁纸生成'),
    (['贴纸','宠物'], '创意贴纸生成'),
    (['抽卡','符号'], '创意抽卡/符号生成'),
    (['红包','封面'], '节日动态封面生成'),
    (['姿态','骨骼','舞蹈','跳舞'], '姿态/动作驱动生成'),
    (['人像','写真','摄影'], '人像写真图像生成'),
    (['分区生成','区域','gligen'], '区域/条件控制图像生成'),
    (['像素图','像素风'], '像素风格图像生成'),
    (['基因融合'], '人物基因/面部融合'),
    (['表情控制','多表情'], '多表情批量生成'),
    (['实时设计','实时渲染','instant'], '实时图像设计工具'),
    (['批量','多张'], '批量多图生成'),
    (['提示词反推','生成提示词','反推'], '图像提示词反推/生成'),
    (['文生图','生图','txt2img','一句话ai'], 'SD 文生图（文字转图像）'),
    (['新手入门必看','必看'], 'ComfyUI 入门基础教程示例'),
    (['lcm绘画','lcm_绘画','lcm实时'], 'LCM 高速实时图像生成'),
    (['turbo','sdxl-turbo','sdxl_turbo'], 'SDXL-Turbo 极速图像生成'),
    (['img2img','图生图'], 'SD 图生图（img2img）'),
    (['ella','驯服提示词'], 'ELLA 增强文本理解工作流'),
    (['xy_表','xy表','xy_plot'], 'XY 参数对比工作流'),
    (['compare_conditioning','compare'], '效果对比工作流'),
    (['在潜空间','潜空间放大'], '潜空间图像放大（Hires Fix）'),
    (['cascade文生图','cascade'], 'Cascade/Würstchen 文生图'),
    (['风格融合','大模型融合'], '多模型/风格融合生成'),
    (['提取器','passes提取','controlnet_passes'], 'ControlNet 预处理图批量提取'),
    (['加载lora'], 'LoRA 加载/叠加入门示例'),
    (['ipadapter_basic','ipadapter_img'], 'IPAdapter 图像参考（入门示例）'),
    (['上妆','美妆','妆容','化妆'],    'AI 美妆/上妆效果生成'),
    (['发型','发色'],                  '发型/发色风格生成'),
    (['修手','手部修复','手崩','脸崩'], '手部/面部修复增强'),
    (['皮肤细节','皮肤放大'],          '皮肤细节超分放大'),
    (['全能工作流','通用工作流','标准生成'], '通用扩散生成工作流'),
    (['混合图像','混合生成'],           '多图混合/融合生成'),
    (['basic_workflow','basic_lora','basic_parametrized','basic_latent'], 'ComfyUI 基础文生图（入门示例）'),
    (['compare_checkpoint','compare_sampler'], '模型/采样器效果对比'),
    (['sdxl_advanced','sdxl_base','sdxl_simple','sdxl_text','sdxl_refiner','sdxl_img','revision_sdxl','unclip_sdxl','img2img_sdxl'], 'SDXL 文生图/图生图工作流'),
    (['conditioning_area','conditioning_average','conditioning_concat','conditioning_style','conditioning_unclip','timestepping'], 'Conditioning 高级控制示例'),
    (['embeddings','clip_skip','blank_token','word_weighting','horrors_negative'], '提示词/嵌入词技巧示例'),
    (['upscale_latent','upscale_pixel','denoise_impact'], '潜空间放大/降噪示例'),
    (['multiple_lora','lora串联'], '多 LoRA 叠加示例'),
    (['gligen','area_vs'], 'GLIGEN/区域控制示例'),
    (['save_noise'], '噪声步骤可视化示例'),
]

LABEL_SHORT = {
    'ckpt':'','lora':'LoRA','controlnet':'CN','ipadapter':'IPA',
    'upscaler':'Up','clip_vision':'CLIPv','vae':'VAE','detector':'Det',
    'sam':'SAM','face_restore':'FR','instantid':'IID','photomaker':'PM',
}

# 自动分类：从检测到的功能标签推断显示分组
CAT_ORDER = [
    'AI动画视频', 'AI换脸人像', 'AI电商换装', 'AI换背景抠图',
    'AI画质修复', 'AI 2D→3D', 'AI室内设计', 'AI摄影写真',
    'AI文字艺术', 'AI线稿绘画', 'AI创意趣玩', '入门基础',
]

CAT_EMOJI = {
    'AI动画视频':  '🎬', 'AI换脸人像': '🧑', 'AI电商换装': '👗',
    'AI换背景抠图':'✂️', 'AI画质修复': '🔧', 'AI 2D→3D':  '🎲',
    'AI室内设计':  '🏠', 'AI摄影写真': '📷', 'AI文字艺术': '✍️',
    'AI线稿绘画':  '✏️', 'AI创意趣玩': '🎨', '入门基础':  '📖',
}


def infer_cat(funcs, stem):
    has = lambda *tags: any(t in funcs for t in tags)
    sl = stem.lower()
    if has('SVD图生视频','AnimateDiff','DragNUWA运动视频','MagicAnimate动作驱动','DynamiCrafter文生视频','SparseCtrl运动控制'):
        return 'AI动画视频'
    if has('ReActor换脸','Roop换脸','InstantID人像','PhotoMaker换脸'):
        return 'AI换脸人像'
    if has('OOTDiffusion换装'):
        return 'AI电商换装'
    if has('RemBG去背','BiRefNet精细抠图','SAM语义分割','LayeredDiffusion透明背景'):
        return 'AI换背景抠图'
    if has('SUPIR超分辨率','CCSR超分辨率','UltimateSD放大','迭代超分放大','模型超分放大','Fooocus智能重绘','BrushNet笔刷重绘','局部重绘Inpaint'):
        return 'AI画质修复'
    if has('Zero123三维视图','SV3D三维视图','TripoSR图转3D'):
        return 'AI 2D→3D'
    if any(k in sl for k in ['室内','建筑','装修','毛坯']):
        return 'AI室内设计'
    if any(k in sl for k in ['写真','摄影','aix','ai摄影']):
        return 'AI摄影写真'
    if any(k in sl for k in ['文字','艺术字','logo','文字特效','造字','广告']):
        return 'AI文字艺术'
    if any(k in sl for k in ['线稿','手绘','草稿']):
        return 'AI线稿绘画'
    if any(k in sl for k in ['新手入门','必看','basic_workflow','basic_lora','basic_latent','basic_parametrized',
                              'compare_checkpoint','compare_sampler','sdxl_advanced','sdxl_base','sdxl_simple',
                              'sdxl_text','sdxl_refiner','embeddings','clip_skip','conditioning_',
                              'upscale_latent','upscale_pixel','save_noise','gligen','area_vs','multiple_lora']):
        return '入门基础'
    return 'AI创意趣玩'


def extract(path):
    try:
        with open(path, encoding='utf-8') as fp: data = json.load(fp)
    except: return [], {}
    if isinstance(data, dict) and 'nodes' in data:
        nodes = data['nodes']
        get_type = lambda n: str(n.get('type',''))
        get_wv   = lambda n: n.get('widgets_values',[])
    elif isinstance(data, dict):
        nodes = [v for v in data.values() if isinstance(v,dict) and 'class_type' in v]
        get_type = lambda n: str(n.get('class_type',''))
        def get_wv(n):
            inp = n.get('inputs',{}); return list(inp.values()) if isinstance(inp,dict) else []
    else:
        return [], {}
    func_tags, seen = [], set()
    models = defaultdict(set)
    for node in nodes:
        t = get_type(node); tl = t.lower(); wv = get_wv(node)
        if t in MODEL_LOADERS:
            for idx, label in MODEL_LOADERS[t]:
                if isinstance(wv,list) and idx < len(wv):
                    val = wv[idx]
                    if isinstance(val,str) and val.strip() and not val.startswith('{') and val not in ('None','On','Off','none',''):
                        models[label].add(val.strip())
        for pat, tag in FUNC_MAP:
            if pat in tl and tag not in seen:
                seen.add(tag); func_tags.append(tag)
    return func_tags, dict(models)


def cn_type(funcs, models=None):
    has = lambda *kws: any(any(kw in f for kw in kws) for f in funcs)
    if has('IC_Light'):       return 'IC-Light 光影控制生成'
    if has('CN_Tile'):        return 'ControlNet Tile 高清重绘'
    if has('CN_Pose'):        return 'ControlNet 姿态控制生成'
    if has('CN_Depth'):       return 'ControlNet 深度图引导生成'
    if has('CN_Lineart'):     return 'ControlNet 线稿引导生成'
    if has('CN_Canny'):       return 'ControlNet Canny 边缘引导'
    if has('CN_SoftEdge'):    return 'ControlNet 软边缘引导生成'
    if has('CN_Inpaint_CN'):  return 'ControlNet Inpaint 精准重绘'
    if has('CN_Scribble'):    return 'ControlNet 涂鸦引导生成'
    if has('CN_Shuffle'):     return 'ControlNet 风格混洗生成'
    if has('CN_Seg'):         return 'ControlNet 语义分割引导'
    if models:
        cn_m = ' '.join(n.lower() for n in models.get('controlnet', set()))
        if 'tile'      in cn_m: return 'ControlNet Tile 高清重绘'
        if 'openpose'  in cn_m or '_pose' in cn_m: return 'ControlNet 姿态控制生成'
        if 'depth'     in cn_m or 'midas' in cn_m: return 'ControlNet 深度图引导生成'
        if 'lineart'   in cn_m: return 'ControlNet 线稿引导生成'
        if 'canny'     in cn_m: return 'ControlNet Canny 边缘引导'
        if 'softedge'  in cn_m or 'hed' in cn_m: return 'ControlNet 软边缘引导生成'
        if 'inpaint'   in cn_m: return 'ControlNet Inpaint 精准重绘'
        if 'qrcode'    in cn_m: return 'ControlNet QR码特效'
        if 'brightness' in cn_m or 'recolor' in cn_m: return 'IC-Light/Recolor 光影重打光'
    return 'ControlNet 引导图像生成'


def ipa_type(models):
    names = ' '.join(n.lower() for n in models.get('ipadapter', set()))
    if 'faceid' in names: return 'IPAdapter FaceID 人脸一致性生成'
    if 'face'   in names: return 'IPAdapter 人脸参考生成'
    if 'plus'   in names: return 'IPAdapter+ 增强风格参考'
    if 'light'  in names: return 'IPAdapter Light 轻量参考'
    return 'IPAdapter 图像风格参考'


def make_desc(stem, funcs, models):
    has    = lambda *kws: any(any(kw in f for kw in kws) for f in funcs)
    sl     = stem.lower()
    fn_has = lambda *kws: any(k.lower() in sl for k in kws)
    chosen = []

    PURPOSE_OVERRIDES = [
        (['扩图','外扩','outpainting','outpaint'],  '图像外扩 (Outpainting)'),
        (['视频转绘','视频转视频','视频风格'],         '视频风格转绘'),
        (['线稿上色','线稿转图','转手绘'],            '线稿/草图转彩色图像'),
        (['实时绘画','魔法画布'],                    '实时草图/绘画生成'),
        (['室内设计','户外设计','建筑渲染'],           '室内/建筑效果图生成'),
        (['二维码'],                              '艺术二维码生成'),
        (['大头q版','大头卡通','chibi'],            'Q版/大头卡通形象生成'),
        (['换人物背','换人物'],                     '人物背景替换'),
        (['证件照','idphoto','id_photo'],          '证件照自动生成'),
        (['换脸','换头','face swap'],              '人脸替换/换脸'),
        (['珠宝设计','首饰设计','珠宝制作','珠宝灵感'], '珠宝/首饰设计生成'),
        (['换装','换衣','试装','服装换','换特定'],     '虚拟换装'),
        (['换背景','更换背景','替换背景'],             '背景替换'),
        (['微观世界'],                            '微观世界创意风格生成'),
        (['壁纸'],                               '创意壁纸图像生成'),
        (['playground'],                          'Playground V2.5 图像生成'),
        (['终极创意'],                            '综合创意特效图像生成'),
        (['手绘风格','手绘转'],                    '图像转手绘风格'),
        (['t恤定制','t恤印花','印花机'],            'T恤/服装印花生成'),
        (['添加服装'],                            '服装虚拟穿戴'),
        (['像素级放大','像素级图片','upscale_by','compare_upscale','denoise_impact_on_pixel',
          '图片放大工作流','sdxl_图片放大','图像放大工作流'], '图像放大/超分辨率示例'),
    ]
    for kws, label in PURPOSE_OVERRIDES:
        if any(k.lower() in sl for k in kws):
            chosen.append(label); break

    if has('SVD图生视频'):
        if fn_has('视角旋转'): chosen.append('SVD 多角度视图旋转动画')
        elif fn_has('红包','封面'): chosen.append('SVD 动态封面生成')
        elif fn_has('xt','svd_xt','25帧'): chosen.append('SVD XT 长视频生成')
        elif fn_has('最小闭环','基础版','入门','svd_workflow','workflow_','basic','get_image_size'):
            chosen.append('SVD 图生视频（基础教程）')
        elif fn_has('平滑','smooth','低帧','短片'): chosen.append('SVD 平滑图生视频')
        else: chosen.append('SVD 图像转视频')

    if has('AnimateDiff'):
        if has('SparseCtrl运动控制'): chosen.append('AnimateDiff SparseCtrl 稀疏运动控制')
        elif has('视频输入') or fn_has('视频转绘','视频转视频','vid2vid'):
            chosen = [c for c in chosen if c != '视频风格转绘']
            chosen.append('AnimateDiff 视频风格转绘')
        elif fn_has('gif','动图','动画gif'): chosen.append('AnimateDiff 文本转 GIF 动图')
        elif fn_has('关键帧','keyframe'): chosen.append('AnimateDiff 关键帧引导动画')
        elif fn_has('生命','女孩','25秒','叙事','故事'): chosen.append('AnimateDiff 长序列叙事动画')
        elif fn_has('文生视频','文本生成视频','txt2video'): chosen.append('AnimateDiff 文字驱动视频')
        elif fn_has('丝滑','smooth','无闪烁'): chosen.append('AnimateDiff 丝滑流畅动画')
        elif fn_has('标准','含lora','lora'): chosen.append('AnimateDiff 标准 LoRA 动画生成')
        else: chosen.append('AnimateDiff 动画生成')
    if has('DynamiCrafter文生视频'): chosen.append('DynamiCrafter 图像引导视频生成')
    if has('DragNUWA运动视频'):      chosen.append('DragNUWA 轨迹控制视频')
    if has('MagicAnimate动作驱动'):  chosen.append('MagicAnimate 姿态驱动动画')
    if has('视频帧插值') and not chosen: chosen.append('视频帧插值补帧')

    def _replace_or_add(old_label, new_label):
        for i, c in enumerate(chosen):
            if old_label in c: chosen[i] = new_label; return
        chosen.append(new_label)

    if has('ReActor换脸'):
        label = 'ReActor 视频换脸' if (has('视频输入') or fn_has('视频')) else 'ReActor 人脸替换'
        _replace_or_add('人脸替换/换脸', label)
    if has('Roop换脸') and not any('换脸' in c for c in chosen):
        chosen.append('Roop 人脸替换')
    if has('InstantID人像'):   chosen.append('InstantID 人像风格迁移')
    if has('PhotoMaker换脸'):  chosen.append('PhotoMaker 人像生成')

    if has('Zero123三维视图'):   chosen.append('Zero123 多角度三维视图')
    elif has('SV3D三维视图'):    chosen.append('SV3D 三维旋转视图')
    elif has('TripoSR图转3D'):   chosen.append('TripoSR 图像转 3D 网格')

    if has('OOTDiffusion换装'):
        _replace_or_add('虚拟换装', 'OOTDiffusion 虚拟换装')

    if has('IPAdapter参考'):
        ipa = ipa_type(models)
        if not chosen or not any('IPA' in c or 'IPAdapter' in c or '参考' in c for c in chosen):
            chosen.append(ipa)

    if has('PortraitMaster人像精修') and not chosen:
        chosen.append('PortraitMaster 人像精修生成')

    if has('ControlNet引导') and not any('SparseCtrl' in c for c in chosen):
        cn = cn_type(funcs, models)
        if not chosen or (len(chosen) < 2 and not any('ControlNet' in c or 'IC-Light' in c for c in chosen)):
            chosen.append(cn)

    if has('IC_Light') and not any('IC-Light' in c or 'ControlNet' in c for c in chosen):
        chosen.append('IC-Light 光影重打光')

    if has('SUPIR超分辨率'):   chosen.append('SUPIR 超分辨率放大')
    elif has('CCSR超分辨率'):  chosen.append('CCSR 超分辨率放大')
    elif has('UltimateSD放大') and not chosen:
        chosen.append('UltimateSD Tile 高清重绘' if has('CN_Tile') else 'UltimateSD 高清放大')
    elif has('迭代超分放大') and not chosen: chosen.append('迭代超分放大')
    elif has('模型超分放大') and not chosen:
        if fn_has('老照片','旧照片'): chosen.append('老照片超分放大修复')
        elif fn_has('人像','人物','面部','脸'): chosen.append('人像图超分放大')
        elif fn_has('动漫','漫画','二次元'): chosen.append('动漫图超分放大')
        else: chosen.append('模型超分放大')

    if has('LayeredDiffusion透明背景'): chosen.append('Layered Diffusion 透明背景生成')
    if has('BrushNet笔刷重绘') and not any('BrushNet' in c or '重绘' in c for c in chosen):
        chosen.append('BrushNet 笔刷区域重绘' if chosen else 'BrushNet 精准笔刷重绘')
    if has('RemBG去背'):
        chosen.append('RemBG 去背' if chosen else 'RemBG 自动去背景/抠图')
    elif has('BiRefNet精细抠图'):
        chosen.append('BiRefNet 抠图' if chosen else 'BiRefNet 精细人物抠图')
    elif has('SAM语义分割') and not chosen: chosen.append('SAM 语义分割/抠图')
    elif has('CLIPSeg文字分割') and not chosen: chosen.append('CLIPSeg 文字引导分割')

    if has('Fooocus智能重绘') and not chosen:  chosen.append('Fooocus Inpaint 智能重绘')
    elif has('局部重绘Inpaint') and not chosen: chosen.append('局部区域重绘 (Inpaint)')

    if has('StyleAligned风格对齐'): chosen.append('StyleAligned 多图同风格批量')
    if has('WD14自动标注') and not chosen:   chosen.append('WD14 自动标注图像')
    if has('CLIP反推提示词') and not chosen:  chosen.append('CLIP 反推提示词')
    if has('漫画/图像网格排版') and not chosen: chosen.append('漫画分格/图像网格排版')
    if has('多表情/图像网格生成') and not chosen: chosen.append('多表情/情绪矩阵批量生成')
    if has('文字图像叠加') and not chosen:    chosen.append('文字图像叠加合成')

    VIDEO_TERMS = ('SVD','AnimateDiff','GIF','动图','视频','动画','DynamiCrafter','DragNUWA','MagicAnimate')
    if has('视频输出') and not any(any(t in c for t in VIDEO_TERMS) for c in chosen):
        chosen.append('输出为视频格式')

    if not chosen or chosen == ['输出为视频格式']:
        for kws, label in FILENAME_FALLBACKS:
            if any(k.lower() in sl for k in kws):
                chosen.insert(0, label); break

    if not chosen:
        chosen.append('扩散模型图像生成' if has('__ksampler__') else 'ComfyUI 工作流')

    if has('FaceDetailer') and chosen and len(chosen) < 3:
        if not any('面部细节增强' in c or 'FaceDetailer' in c for c in chosen):
            chosen.append('＋面部细节增强')

    if chosen and len(chosen) < 3:
        if has('UltimateSD放大') and not any('放大' in c or '高清' in c or 'UltimateSD' in c for c in chosen):
            chosen.append('＋UltimateSD 放大')
        elif has('模型超分放大') and not any('放大' in c or '超分' in c for c in chosen):
            chosen.append('＋超分放大')

    seen2, result = set(), []
    for c in chosen:
        if c not in seen2: seen2.add(c); result.append(c)
    return '、'.join(result[:3])


def fmt_models(models):
    import re as _re
    def _clean(n):
        n = _re.split(r'[/\\]', n)[-1]
        n = _re.sub(r'@[0-9a-f]{6,}', '', n)
        n = _re.sub(r'\.(safetensors|ckpt|pt|bin|pth)$', '', n, flags=_re.I)
        return n.strip()
    SHOW = [('ckpt',1,''),('lora',1,'LoRA'),('ipadapter',1,'IPA'),
            ('controlnet',1,'CN'),('upscaler',1,'Up'),
            ('instantid',1,'IID'),('photomaker',1,'PM'),('face_restore',1,'FR')]
    HIDE = {'vae','clip_vision','sam','detector'}
    parts=[]; total=0; skipped=0
    for label,lim,short in SHOW:
        names=sorted(models.get(label,[]))
        for n in names[:lim]:
            if total>=3: skipped+=1; continue
            d=_clean(n); d=d if len(d)<=34 else d[:31]+'…'
            parts.append(f'`{d}`'+(f' ({short})' if short else ''))
            total+=1
        skipped+=max(0,len(names)-lim)
    for lbl in HIDE:
        skipped+=len(models.get(lbl,[]))
    result=' · '.join(parts) if parts else '—'
    if skipped>0: result+=f' _(+{skipped})_'
    return result


# ── 主流程 ────────────────────────────────────────────────────
all_files = sorted(BASE.glob('*.json'))
groups = defaultdict(list)

for path in all_files:
    if path.name == 'index.json':
        continue
    funcs, models = extract(path)
    desc = make_desc(path.stem, funcs, models)
    cat  = infer_cat(funcs, path.stem)
    groups[cat].append((path.stem, desc, models))

dist = Counter()
for items in groups.values():
    for _, desc, _ in items:
        dist['扩散兜底' if desc in ('扩散模型图像生成','ComfyUI 工作流') else '有效'] += 1
print(f"描述质量: {dict(dist)}")

all_descs = [desc for items in groups.values() for _, desc, _ in items]
top = Counter(all_descs).most_common(12)
print("\n高频描述 TOP12:")
for d, n in top:
    print(f"  {n:3d}x  {d}")

gen_date = datetime.now().strftime('%Y-%m-%d')
total = sum(len(v) for v in groups.values())
lines = ['# ComfyUI 工作流索引\n',
         f'> 自动生成 · 按内容分类 · 共 {total} 个工作流 · 更新于 {gen_date}\n', '---\n']

cat_totals = {cat: len(items) for cat, items in groups.items()}

for cat in CAT_ORDER:
    items = groups.get(cat)
    if not items:
        continue
    emoji = CAT_EMOJI.get(cat, '')
    lines.append(f'\n## {emoji} {cat}（{len(items)} 个）\n')
    lines += ['| 工作流文件 | 作用描述 | 主要模型 |',
              '|-----------|---------|---------|']
    for stem, desc, mdls in sorted(items):
        lines.append(f'| {stem} | {desc} | {fmt_models(mdls)} |')

# 未覆盖分类
for cat, items in groups.items():
    if cat not in CAT_ORDER:
        lines.append(f'\n## {cat}（{len(items)} 个）\n')
        lines += ['| 工作流文件 | 作用描述 | 主要模型 |',
                  '|-----------|---------|---------|']
        for stem, desc, mdls in sorted(items):
            lines.append(f'| {stem} | {desc} | {fmt_models(mdls)} |')

content = '\n'.join(lines) + '\n'
OUT.write_text(content, encoding='utf-8')
print(f'\n✅ 写入 {OUT}  ({len(content)//1024} KB)')

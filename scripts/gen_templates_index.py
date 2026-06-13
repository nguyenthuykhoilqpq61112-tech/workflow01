"""
生成 templates/index.json（官方 Comfy-Org/workflow_templates 格式）

从 templates/*.json 读取工作流，自动分类后写入 index.json。

用法：
  python scripts/gen_templates_index.py
  python scripts/gen_templates_index.py --dry-run
"""

import json, sys
from pathlib import Path
from collections import defaultdict
from datetime import date

ROOT      = Path(__file__).resolve().parent.parent
TEMPLATES = ROOT / "templates"
INDEX_OUT = TEMPLATES / "index.json"
DRY_RUN   = "--dry-run" in sys.argv

# ─── 模型加载器识别表 ─────────────────────────────────────────────────────────
MODEL_LOADERS = {
    "CheckpointLoaderSimple":           [(0, "ckpt")],
    "CheckpointLoader":                 [(0, "ckpt")],
    "ImageOnlyCheckpointLoader":        [(0, "ckpt")],
    "Efficient Loader":                 [(0, "ckpt")],
    "LoraLoader":                       [(0, "lora")],
    "LoraLoaderModelOnly":              [(0, "lora")],
    "Load Lora":                        [(0, "lora")],
    "LoRALoader":                       [(0, "lora")],
    "ControlNetLoader":                 [(0, "controlnet")],
    "DiffControlNetLoader":             [(0, "controlnet")],
    "ControlNetLoaderAdvanced":         [(0, "controlnet")],
    "IDControlNetLoader":               [(0, "controlnet")],
    "IPAdapterModelLoader":             [(0, "ipadapter")],
    "IPAdapterUnifiedLoader":           [(0, "ipadapter")],
    "UpscaleModelLoader":               [(0, "upscaler")],
    "CLIPVisionLoader":                 [(0, "clip_vision")],
    "VAELoader":                        [(0, "vae")],
    "UltralyticsDetectorProvider":      [(0, "detector")],
    "SAMLoader":                        [(0, "sam")],
    "SAMModelLoader (segment anything)":[(0, "sam")],
    "FaceRestoreModelLoader":           [(0, "face_restore")],
    "InstantIDModelLoader":             [(0, "instantid")],
    "PhotoMakerLoader":                 [(0, "photomaker")],
    "PhotoMakerAdapter_Loader_local":   [(0, "photomaker")],
    "PhotoMakerAdapter_Loader_fromhub": [(0, "photomaker")],
    "CCSR_Model_Select":                [(0, "upscaler")],
    "Load CheckPoint DragNUWA":         [(0, "ckpt")],
    "CR Multi-ControlNet Stack":        [(1, "controlnet")],
    "CR ControlNet Stack":              [(1, "controlnet")],
    "MagicAnimateModelLoader":          [(0, "ckpt")],
}

# ─── 功能节点 → 特征标签 ──────────────────────────────────────────────────────
FUNC_MAP = [
    ("svd_img2vid_conditioning",         "SVD"),
    ("ade_animatediffloaderwithcontext", "AnimateDiff"),
    ("ade_animatediffloader",            "AnimateDiff"),
    ("ade_applyanimatediffmodel",        "AnimateDiff"),
    ("ade_useevolvedsampling",           "AnimateDiff"),
    ("ade_animatediffloadertextmatch",   "AnimateDiff"),
    ("workflow/animate",                 "AnimateDiff"),
    ("dragnuwa run",                     "DragNUWA"),
    ("load checkpoint dragnuwa",         "DragNUWA"),
    ("magicanimate",                     "MagicAnimate"),
    ("vhs_loadvideo",                    "VideoInput"),
    ("vhs_loadvideopath",                "VideoInput"),
    ("vhs_videocombine",                 "VideoOutput"),
    ("reactorfaceswap",                  "ReActor"),
    ("reactor",                          "ReActor"),
    ("roop",                             "Roop"),
    ("idgenerationnode",                 "InstantID"),
    ("idbasemodelloader",                "InstantID"),
    ("applyinstantid",                   "InstantID"),
    ("instantidfaceanalysis",            "InstantID"),
    ("insightfaceloader_zho",            "InstantID"),
    ("ipadapter_instantidloader",        "InstantID"),
    ("new_photomaker_generation",        "PhotoMaker"),
    ("photomakeradapter_loader",         "PhotoMaker"),
    ("photomakerloader",                 "PhotoMaker"),
    ("zero123",                          "Zero123"),
    ("sv3d",                             "SV3D"),
    ("triposr",                          "TripoSR"),
    ("loadootdpipeline",                 "OOTDiffusion"),
    ("ootdgenerate",                     "OOTDiffusion"),
    ("supir_upscale",                    "SUPIR"),
    ("ccsr_upscale",                     "CCSR"),
    ("ultimatesdupscale",                "UltimateSD"),
    ("facedetailer",                     "FaceDetailer"),
    ("segsdetailerforanimatediff",       "FaceDetailerVideo"),
    ("groundingdinosamsegment",          "SAM"),
    ("groundingdinomodelloader",         "SAM"),
    ("samdetector",                      "SAM"),
    ("image rembg",                      "RemBG"),
    ("image remove background",          "RemBG"),
    ("rembgsession",                     "RemBG"),
    ("layermask: birefnet",              "BiRefNet"),
    ("birefnetultra",                    "BiRefNet"),
    ("layereddiffusionapply",            "LayeredDiffusion"),
    ("layereddiffusiondecode",           "LayeredDiffusion"),
    ("inpaint_applyfooocusinpaint",      "FooocusInpaint"),
    ("inpaint_loadinpaintmodel",         "FooocusInpaint"),
    ("brushnet",                         "BrushNet"),
    ("vaeencodeforinpaint",              "Inpaint"),
    ("ipadapteradvanced",                "IPAdapter"),
    ("ipadapterapply",                   "IPAdapter"),
    ("ipadapterfaceid",                  "IPAdapter"),
    ("ipadapterapplyfaceid",             "IPAdapter"),
    ("stylealignedbatchalign",           "StyleAligned"),
    ("controlnetapply",                  "ControlNet"),
    ("controlnetapplyadvanced",          "ControlNet"),
    ("cr multi-controlnet stack",        "ControlNet"),
    ("acn_advancedcontrolnet",           "ControlNet"),
    ("t2i-adapter",                      "ControlNet"),
    ("dynamicrafterloader",              "DynamiCrafter"),
    ("dynamicrafterprocessor",           "DynamiCrafter"),
    ("acn_sparsectrlloaderadvanced",     "SparseCtrl"),
    ("ic-light",                         "ICLight"),
    ("iclight",                          "ICLight"),
    ("ksampler",                         "KSampler"),
]

# ─── 特征 → 英文描述 ──────────────────────────────────────────────────────────
FEATURE_EN = {
    "SVD":            "SVD image-to-video",
    "AnimateDiff":    "AnimateDiff animation",
    "DragNUWA":       "DragNUWA motion video",
    "MagicAnimate":   "MagicAnimate pose-driven animation",
    "ReActor":        "ReActor face swap",
    "Roop":           "Roop face swap",
    "InstantID":      "InstantID portrait transfer",
    "PhotoMaker":     "PhotoMaker portrait generation",
    "Zero123":        "Zero123 multi-view 3D",
    "SV3D":           "SV3D 3D rotation view",
    "TripoSR":        "TripoSR image-to-3D mesh",
    "OOTDiffusion":   "OOTDiffusion virtual try-on",
    "SUPIR":          "SUPIR super-resolution upscale",
    "CCSR":           "CCSR super-resolution upscale",
    "UltimateSD":     "UltimateSD high-res refinement",
    "FaceDetailer":   "FaceDetailer face enhancement",
    "SAM":            "SAM semantic segmentation",
    "RemBG":          "RemBG background removal",
    "BiRefNet":       "BiRefNet precise matting",
    "LayeredDiffusion":"Layered Diffusion transparent background",
    "FooocusInpaint": "Fooocus smart inpainting",
    "BrushNet":       "BrushNet brush inpainting",
    "Inpaint":        "local inpainting",
    "IPAdapter":      "IPAdapter image reference",
    "StyleAligned":   "StyleAligned multi-image style consistency",
    "ControlNet":     "ControlNet guided generation",
    "DynamiCrafter":  "DynamiCrafter image-guided video",
    "SparseCtrl":     "SparseCtrl motion control",
    "ICLight":        "IC-Light relighting",
    "KSampler":       "diffusion image generation",
}

# ─── 特征 → tags ──────────────────────────────────────────────────────────────
FEATURE_TAGS = {
    "SVD":            ["Image to Video"],
    "AnimateDiff":    ["Video", "Animation"],
    "DragNUWA":       ["Video"],
    "MagicAnimate":   ["Video", "Animation"],
    "ReActor":        ["Face Swap"],
    "Roop":           ["Face Swap"],
    "InstantID":      ["Portrait", "Face Consistency"],
    "PhotoMaker":     ["Portrait"],
    "Zero123":        ["3D Model"],
    "SV3D":           ["3D Model"],
    "TripoSR":        ["3D Model"],
    "OOTDiffusion":   ["Fashion", "Virtual Try-On"],
    "SUPIR":          ["Upscale"],
    "CCSR":           ["Upscale"],
    "UltimateSD":     ["Upscale"],
    "RemBG":          ["Background Removal"],
    "BiRefNet":       ["Background Removal"],
    "LayeredDiffusion":["Background Removal"],
    "IPAdapter":      ["Image Reference"],
    "StyleAligned":   ["Style Transfer"],
    "ControlNet":     ["ControlNet"],
    "DynamiCrafter":  ["Video"],
    "SparseCtrl":     ["Video", "Animation"],
    "ICLight":        ["Lighting"],
    "Inpaint":        ["Inpainting"],
    "BrushNet":       ["Inpainting"],
    "FooocusInpaint": ["Inpainting"],
}

# ─── 自动分类：特征集 + 文件名 → 分类 key ─────────────────────────────────────
CATEGORY_ENTRIES = {
    "video": {
        "title": "AI Animation & Video | 动画视频",
        "type":  "video",
        "icon":  "icon-[lucide--film]",
        "tags":  ["Video", "Animation"],
    },
    "face": {
        "title": "AI Face & Portrait | 换脸人像",
        "type":  "image",
        "icon":  "icon-[lucide--user]",
        "tags":  ["Face Swap", "Portrait"],
    },
    "fashion": {
        "title": "AI Fashion & Try-On | 电商换装",
        "type":  "image",
        "icon":  "icon-[lucide--shirt]",
        "tags":  ["Fashion", "Virtual Try-On"],
    },
    "matting": {
        "title": "AI Background & Matting | 换背景抠图",
        "type":  "image",
        "icon":  "icon-[lucide--scissors]",
        "tags":  ["Image", "Background Removal"],
    },
    "upscale": {
        "title": "AI Upscale & Repair | 画质修复",
        "type":  "image",
        "icon":  "icon-[lucide--wrench]",
        "tags":  ["Image", "Upscale", "Restoration"],
    },
    "3d": {
        "title": "AI 2D to 3D | 2D转3D",
        "type":  "image",
        "icon":  "icon-[lucide--box]",
        "tags":  ["3D Model"],
    },
    "interior": {
        "title": "AI Interior Design | 室内设计",
        "type":  "image",
        "icon":  "icon-[lucide--home]",
        "tags":  ["Image", "Interior Design"],
    },
    "photography": {
        "title": "AI Photography | 摄影写真",
        "type":  "image",
        "icon":  "icon-[lucide--camera]",
        "tags":  ["Image", "Photography"],
    },
    "creative": {
        "title": "AI Creative & Text Art | 创意文字",
        "type":  "image",
        "icon":  "icon-[lucide--palette]",
        "tags":  ["Image", "Creative"],
    },
    "general": {
        "title": "AI Image Generation | 图像生成",
        "type":  "image",
        "icon":  "icon-[lucide--image]",
        "tags":  ["Image"],
    },
}

CATEGORY_ORDER = ["video", "face", "fashion", "matting", "upscale", "3d",
                  "interior", "photography", "creative", "general"]


def infer_category(features: set, stem: str) -> str:
    sl = stem.lower()
    if features & {"SVD", "AnimateDiff", "DragNUWA", "MagicAnimate", "DynamiCrafter", "SparseCtrl"}:
        return "video"
    if features & {"ReActor", "Roop", "InstantID", "PhotoMaker"}:
        return "face"
    if features & {"OOTDiffusion"} or any(k in sl for k in ["换装","换衣","试装"]):
        return "fashion"
    if features & {"RemBG", "BiRefNet", "LayeredDiffusion", "SAM"} or any(k in sl for k in ["抠图","去背","换背景"]):
        return "matting"
    if features & {"SUPIR", "CCSR", "UltimateSD", "FooocusInpaint", "BrushNet"} or any(k in sl for k in ["超分","放大","重绘","修复"]):
        return "upscale"
    if features & {"Zero123", "SV3D", "TripoSR"} or any(k in sl for k in ["3d","三维","三视图","多视角"]):
        return "3d"
    if any(k in sl for k in ["室内","建筑","装修","毛坯"]):
        return "interior"
    if any(k in sl for k in ["写真","摄影","aix","ai摄影"]):
        return "photography"
    if any(k in sl for k in ["文字","艺术字","logo","线稿","手绘","创意","漫画","卡通","粘土","壁纸"]):
        return "creative"
    return "general"


def extract(path: Path):
    try:
        with open(path, encoding="utf-8") as fp:
            data = json.load(fp)
    except Exception:
        return set(), {}

    if isinstance(data, dict) and "nodes" in data:
        nodes = data["nodes"]
        get_type = lambda n: str(n.get("type", ""))
        get_wv   = lambda n: n.get("widgets_values", [])
    elif isinstance(data, dict):
        nodes = [v for v in data.values() if isinstance(v, dict) and "class_type" in v]
        get_type = lambda n: str(n.get("class_type", ""))
        def get_wv(n):
            inp = n.get("inputs", {})
            return list(inp.values()) if isinstance(inp, dict) else []
    else:
        return set(), {}

    features = set()
    models: dict[str, set] = defaultdict(set)

    for node in nodes:
        t = get_type(node); tl = t.lower(); wv = get_wv(node)
        if t in MODEL_LOADERS:
            for idx, label in MODEL_LOADERS[t]:
                if isinstance(wv, list) and idx < len(wv):
                    val = wv[idx]
                    if isinstance(val, str) and val.strip() and val not in ("None","On","Off","none",""):
                        models[label].add(val.strip())
        for pat, feat in FUNC_MAP:
            if pat in tl:
                features.add(feat)

    return features, dict(models)


def make_description(stem: str, features: set) -> str:
    sl = stem.lower()
    priority = [
        "SVD", "AnimateDiff", "DragNUWA", "MagicAnimate", "DynamiCrafter", "SparseCtrl",
        "ReActor", "Roop", "InstantID", "PhotoMaker",
        "Zero123", "SV3D", "TripoSR", "OOTDiffusion",
        "SUPIR", "CCSR", "LayeredDiffusion", "BiRefNet", "RemBG", "SAM",
        "FooocusInpaint", "BrushNet", "ICLight",
        "IPAdapter", "StyleAligned", "ControlNet", "UltimateSD", "Inpaint", "FaceDetailer",
    ]
    chosen = [FEATURE_EN[f] for f in priority if f in features and f in FEATURE_EN][:2]

    if not chosen:
        kw_map = [
            (["换脸","换头"],                  "face swap"),
            (["换装","换衣","试装"],            "virtual try-on"),
            (["换背景","替换背景"],             "background replacement"),
            (["抠图","去背"],                  "background removal / matting"),
            (["超清","超分","高清放大"],         "image upscaling"),
            (["室内设计","建筑"],               "interior design rendering"),
            (["艺术字","文字特效","logo"],       "text / logo art generation"),
            (["老照片","照片修复"],             "old photo restoration"),
            (["线稿","手绘"],                  "line art / sketch guided generation"),
            (["视频转绘","video"],             "video style transfer"),
            (["3d","三维","三视图"],            "3D / multi-view generation"),
            (["写真","摄影","人像"],            "AI portrait photography"),
            (["动画","animation"],             "animation generation"),
        ]
        for kws, label in kw_map:
            if any(k in sl for k in kws):
                chosen.append(label); break

    if not chosen and "KSampler" in features:
        chosen.append("diffusion image generation")

    if not chosen:
        chosen.append("ComfyUI workflow")

    if "FaceDetailer" in features and "FaceDetailerVideo" not in features and len(chosen) < 2:
        chosen.append("+ face enhancement")

    return "; ".join(chosen[:2])


def make_tags(cat_key: str, features: set) -> list:
    tags = list(CATEGORY_ENTRIES[cat_key]["tags"])
    for feat, extra in FEATURE_TAGS.items():
        if feat in features:
            for t in extra:
                if t not in tags:
                    tags.append(t)
    return tags[:6]


def clean_model_name(n: str) -> str:
    import re
    n = n.split("/")[-1].split("\\")[-1]
    n = re.sub(r"@[0-9a-f]{6,}", "", n)
    n = re.sub(r"\.(safetensors|ckpt|pt|bin|pth)$", "", n, flags=re.I)
    return n.strip()[:60]


def make_models_list(models: dict) -> list:
    result = []
    for label in ["ckpt", "lora", "controlnet", "ipadapter", "upscaler"]:
        for n in sorted(models.get(label, []))[:1]:
            clean = clean_model_name(n)
            if clean and clean not in result:
                result.append(clean)
            if len(result) >= 3:
                return result
    return result


def main():
    today = date.today().isoformat()
    all_files = sorted(p for p in TEMPLATES.glob("*.json") if p.name != "index.json")
    print(f"找到 {len(all_files)} 个工作流文件")

    groups: dict[str, list] = defaultdict(list)

    for p in all_files:
        features, models = extract(p)
        cat_key     = infer_category(features, p.stem)
        description = make_description(p.stem, features)
        tags        = make_tags(cat_key, features)
        model_names = make_models_list(models)

        entry = {
            "name":        p.stem,
            "title":       p.stem,
            "description": description,
            "mediaType":   "image",
            "mediaSubtype":"png",
            "tags":        tags,
            "date":        today,
            "openSource":  True,
            "username":    "leo",
        }
        if model_names:
            entry["models"] = model_names

        groups[cat_key].append(entry)

    index = []
    for cat_key in CATEGORY_ORDER:
        templates = groups.get(cat_key, [])
        if not templates:
            continue
        cat_info = CATEGORY_ENTRIES[cat_key]
        index.append({
            "moduleName": "community",
            "title":      cat_info["title"],
            "type":       cat_info["type"],
            "icon":       cat_info["icon"],
            "templates":  templates,
        })

    total = sum(len(c["templates"]) for c in index)
    print(f"类别数: {len(index)},  模板总数: {total}")
    for c in index:
        print(f"  {len(c['templates']):3d}  {c['title']}")

    if not DRY_RUN:
        INDEX_OUT.write_text(
            json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        print(f"\n✅ 写入 {INDEX_OUT}  ({INDEX_OUT.stat().st_size // 1024} KB)")
    else:
        sample = index[0]["templates"][0] if index else {}
        print("\n[dry-run] 示例条目:", json.dumps(sample, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

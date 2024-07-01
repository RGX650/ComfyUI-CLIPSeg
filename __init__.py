# ComfyUI-CLIPSeg/__init__.py

from .clipseg import CLIPSeg, CombineMasks


NODE_CLASS_MAPPINGS = {
    "CLIPSeg": CLIPSeg,
    "CombineSegMasks": CombineMasks,
}

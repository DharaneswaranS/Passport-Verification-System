from .detector import detect_fields
from .region_builder import build_regions
from .cropper import crop_regions
from .ocr import read_all
from .parser import parse_fields

def web(p):
    if not p:return None
    return "/static/"+p.replace("\\","/").split("static/")[-1]

def process_passport(path):

    detections=detect_fields(path)
    regions=build_regions(path,detections)
    crops=crop_regions(path,regions)
    ocr_data=read_all(crops)
    data=parse_fields(ocr_data)

    return {
        "data":data,
        "photo":web(crops.get("photo")),
        "signature":web(crops.get("signature"))
    }

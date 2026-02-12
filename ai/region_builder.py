import cv2

def build_regions(image_path, detections):

    img = cv2.imread(image_path)
    h, w = img.shape[:2]

    photo = mrz = signature = None

    for label,x1,y1,x2,y2 in detections:
        if label=="photo": photo=(x1,y1,x2,y2)
        if label=="mrz": mrz=(x1,y1,x2,y2)
        if label=="signature": signature=(x1,y1,x2,y2)

    regions={}

    # text region above MRZ
    if mrz:
        tx1,ty1,tx2,ty2 = 0,0,w,mrz[1]
        if photo:
            tx1=min(photo[2]+20,w)
        regions["text"]=(tx1,ty1,tx2,ty2)

    # passport number top-right
    if "text" in regions:
        tx1,ty1,tx2,ty2=regions["text"]
        pw=int((tx2-tx1)*0.45)
        ph=int((ty2-ty1)*0.25)
        regions["passport_number"]=(tx2-pw-20,ty1+20,tx2-20,ty1+ph)

    if photo: regions["photo"]=photo
    if signature: regions["signature"]=signature
    if mrz: regions["mrz"]=mrz

    return regions

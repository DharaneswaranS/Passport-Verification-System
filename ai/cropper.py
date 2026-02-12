import cv2, os
from config import OUTPUT_FOLDER

def crop_regions(image_path, regions):

    img=cv2.imread(image_path)
    outputs={}

    for label,(x1,y1,x2,y2) in regions.items():

        x1=max(0,x1); y1=max(0,y1)
        x2=min(img.shape[1],x2); y2=min(img.shape[0],y2)

        crop=img[y1:y2,x1:x2]
        save=os.path.join(OUTPUT_FOLDER,f"{label}.jpg")

        cv2.imwrite(save,crop)
        outputs[label]=save

    return outputs

import easyocr, cv2
reader = easyocr.Reader(['en'], gpu=True)

def read_region(path):
    img=cv2.imread(path)
    if img is None: return ""
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    return "\n".join(reader.readtext(gray,detail=0,paragraph=True))

def read_all(crops):
    data={}
    if "mrz" in crops: data["mrz"]=read_region(crops["mrz"])
    if "passport_number" in crops: data["number"]=read_region(crops["passport_number"])
    if "text" in crops: data["text"]=read_region(crops["text"])
    return data

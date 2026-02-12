from ultralytics import YOLO
import os

model = YOLO(os.path.join("models","passport_layout.pt"))

def detect_fields(image_path):

    results = model(image_path, conf=0.4)[0]

    detections = []
    for box in results.boxes:
        cls = int(box.cls[0])
        label = model.names[cls]
        x1,y1,x2,y2 = map(int, box.xyxy[0])

        detections.append((label,x1,y1,x2,y2))

    return detections

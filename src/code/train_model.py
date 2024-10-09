from ultralytics import YOLO

def train_model():
    # Load a pretrained YOLOv8 model
    model = YOLO("yolov8m.pt")

    # Train the model
    results = model.train(data="data.yaml", epochs=25, imgsz=640)
    return results


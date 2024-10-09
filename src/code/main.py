from ultralytics import YOLO
from prepare_data import prepare_data
from train_model import train_model
from validate_model import validate_model
from run_inference import run_inference
from display_metrics import display_metrics
import os

def main():
    model_path = "runs/detect/train/weights/best.pt"

    if not os.path.exists(model_path):
        prepare_data()
        results = train_model()
    else:
        print(f"Model already trained. Loading from {model_path}")

    model = YOLO(model_path)
    #validate_model(model)
    display_metrics()

    sample_image_path = "C:/Users/Jilen/PycharmProjects/Size Recommendation/src/test1.jpg"
    run_inference(model, image_path=sample_image_path)

if __name__ == "__main__":
    main()





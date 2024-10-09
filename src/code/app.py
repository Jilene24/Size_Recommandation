import streamlit as st
import cv2
import numpy as np
from PIL import Image
from ultralytics import YOLO
import torch

# Load the YOLO model
model_path = "runs/detect/train/weights/best.pt"
model = YOLO(model_path)


def detect_objects(frame):
    resized_frame = cv2.resize(frame, (640, 480))

    # Perform inference
    results = model(resized_frame)

    if isinstance(results, list):
        results = results[0]

    annotated_img = resized_frame.copy()
    boxes = results.boxes.xyxy.cpu().numpy()
    confidences = results.boxes.conf.cpu().numpy()
    labels = results.names

    if isinstance(labels, torch.Tensor):
        labels = labels.cpu().numpy()

    for i, box in enumerate(boxes):
        x1, y1, x2, y2 = map(int, box)
        conf = confidences[i]
        label_id = int(results.boxes.cls.cpu().numpy()[i])
        label = labels[label_id]

        cv2.rectangle(annotated_img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        text = f"{label} {conf:.2f}"
        cv2.putText(annotated_img, text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    return annotated_img


def process_uploaded_file(uploaded_file):
    if uploaded_file.type.startswith('image/'):
        image = Image.open(uploaded_file)
        image_array = np.array(image)
        annotated_img = detect_objects(image_array)
        st.image(annotated_img, caption="Detected Objects", use_column_width=True)

    elif uploaded_file.type.startswith('video/'):
        video_bytes = uploaded_file.read()
        video = cv2.VideoCapture(cv2.imdecode(np.frombuffer(video_bytes, np.uint8), cv2.IMREAD_COLOR))

        if not video.isOpened():
            st.error("Error opening video.")
            return

        stframe = st.empty()
        while True:
            ret, frame = video.read()
            if not ret:
                break

            result_frame = detect_objects(frame)
            stframe.image(result_frame, channels="RGB", use_column_width=True)

        video.release()
        cv2.destroyAllWindows()


def capture_and_detect():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        st.error("Camera not accessible.")
        return None

    stframe = st.empty()
    capture_button = st.button('Capture and Detect', key='capture_button')

    captured_frame = None

    while True:
        ret, frame = cap.read()
        if not ret:
            st.error("Failed to capture image from camera.")
            break

        # Display the live camera feed
        stframe.image(frame, channels="BGR", use_column_width=True)

        # Check if button was pressed
        if capture_button:
            captured_frame = frame
            break

    cap.release()
    cv2.destroyAllWindows()

    if captured_frame is not None:
        annotated_img = detect_objects(captured_frame)
        _, img_encoded = cv2.imencode('.jpg', annotated_img)
        return img_encoded.tobytes()
    return None


def main():
    st.title("Clothes Style Detection ")

    # Upload image or video
    uploaded_file = st.file_uploader("Upload an image or video", type=['jpg', 'jpeg', 'png', 'mp4'])

    if uploaded_file is not None:
        process_uploaded_file(uploaded_file)

    # Capture from webcam
    st.write("Open webcam and capture a frame:")
    result_image = capture_and_detect()
    if result_image:
        st.image(result_image, caption="Detected Objects", use_column_width=True)


if __name__ == "__main__":
    main()

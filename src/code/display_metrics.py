from IPython.display import Image, display

def display_metrics():
    # Display training metrics
    display(Image(filename='runs/detect/train/F1_curve.png'))
    display(Image(filename='runs/detect/train/PR_curve.png'))



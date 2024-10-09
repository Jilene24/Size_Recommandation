import os
import shutil

def prepare_data():
    # Create directories for images and labels
    os.makedirs('images/train', exist_ok=True)
    os.makedirs('images/val', exist_ok=True)
    os.makedirs('labels/train', exist_ok=True)
    os.makedirs('labels/val', exist_ok=True)

    # Define the base directory for your data
    base_dir = 'C:/Users/Jilen/PycharmProjects/Size Recommendation/src/Data3'

    # Define paths to your downloaded dataset
    train_images_src = os.path.join(base_dir, 'train/images')
    val_images_src = os.path.join(base_dir, 'valid/images')
    test_images_src = os.path.join(base_dir, 'test/images')
    train_labels_src = os.path.join(base_dir, 'train/labels')
    val_labels_src = os.path.join(base_dir, 'valid/labels')
    test_labels_src = os.path.join(base_dir, 'test/labels')

    # Copy train images and labels
    shutil.copytree(train_images_src, 'images/train', dirs_exist_ok=True)
    shutil.copytree(val_images_src, 'images/val', dirs_exist_ok=True)
    shutil.copytree(test_images_src, 'images/test', dirs_exist_ok=True)
    shutil.copytree(test_images_src, 'images/test', dirs_exist_ok=True)
    shutil.copytree(train_labels_src, 'labels/train', dirs_exist_ok=True)
    shutil.copytree(val_labels_src, 'labels/val', dirs_exist_ok=True)
    shutil.copytree(test_labels_src, 'labels/test', dirs_exist_ok=True)
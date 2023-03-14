
import os
from PIL import Image


data_path = r"frames"
def check_image_sizes(data_path, desired_size):
    smallest_size = None
    for root, dirs, files in os.walk(data_path):
        for file in files:
            if file.endswith(".jpg") or file.endswith(".png"):
                img_path = os.path.join(root, file)
                with Image.open(img_path) as img:
                    if smallest_size is None or min(img.size) < smallest_size:
                        smallest_size = min(img.size)
                    if img.size != desired_size:
                        print(f"Image {img_path} has size {img.size}, resizing...")
    if smallest_size is not None and smallest_size < min(desired_size):
        print(f"Warning: Some images have a smaller dimension than the desired size ({smallest_size} < {min(desired_size)})")

check_image_sizes(data_path, (224, 224))

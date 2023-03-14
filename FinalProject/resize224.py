import os
from PIL import Image


data_path = "frames"
def preprocess_images(data_path, target_size=(224, 224)):
    for root, dirs, files in os.walk(data_path):
        for file in files:
            if file.endswith(".jpg") or file.endswith(".png"):
                img_path = os.path.join(root, file)
                with Image.open(img_path) as img:
                    if img.size != target_size:
                        resized_img = img.resize(target_size)
                        resized_img.save(img_path)


preprocess_images(data_path, target_size=(224, 224))
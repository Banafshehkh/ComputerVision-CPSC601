

import os

def count_images(data_path):
    for root, dirs, files in os.walk(data_path):
        num_images = len([file for file in files if file.endswith((".jpg", ".jpeg", ".png"))])
        print(f"{root}: {num_images}")

data_path = "frames"
count_images(data_path)

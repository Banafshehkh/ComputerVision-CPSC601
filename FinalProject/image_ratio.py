import os
from PIL import Image

def check_image_sizes(data_path):
    sizes = set()
    for root, dirs, files in os.walk(data_path):
        for file in files:
            if file.endswith(".jpg") or file.endswith(".png"):
                img_path = os.path.join(root, file)
                with Image.open(img_path) as img:
                    sizes.add(img.size)
    return len(sizes) == 1, sizes.pop() if sizes else None


root_dir = r"frames"
same_size = check_image_sizes(root_dir)
print(same_size)

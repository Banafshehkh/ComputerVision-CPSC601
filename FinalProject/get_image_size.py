import os
from PIL import Image

def check_images_size(root_dir):
    """
    Check if all images in all subdirectories of root_dir have the same size.
    Returns True if all images have the same size, False otherwise.
    """
    sizes = set()
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(".jpg") or filename.endswith(".png"):
                path = os.path.join(dirpath, filename)
                with Image.open(path) as img:
                    sizes.add(img.size)
                    if len(sizes) > 1:
                        return False
    return True

root_dir = r"frames"
same_size = check_images_size(root_dir)
print(same_size)

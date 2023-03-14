import os
import random

def keep_random_images(data_path, num_keep=1000):
    for root, dirs, files in os.walk(data_path):
        # Skip the root directory
        if root == data_path:
            continue
        
        # Randomly choose which files to keep
        to_keep = set(random.sample(files, num_keep))
        
        for file in files:
            if file not in to_keep:
                # Delete the file if it's not one of the randomly chosen ones
                os.remove(os.path.join(root, file))


data_path = "frames"
keep_random_images(data_path, num_keep=1000)

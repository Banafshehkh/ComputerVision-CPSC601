import os
import random
import shutil

# set the path to the folder containing subfolders of images
data_folder = "frames"

# set the path to the folder where the train, val, and test folders will be created
split_folder = ""

# set the percentage split for train, val, and test sets
train_split = 0.8
val_split = 0.1
test_split = 0.1

# create the train, val, and test folders
train_folder = os.path.join(split_folder, "train")
val_folder = os.path.join(split_folder, "val")
test_folder = os.path.join(split_folder, "test")
os.makedirs(train_folder, exist_ok=True)
os.makedirs(val_folder, exist_ok=True)
os.makedirs(test_folder, exist_ok=True)

# loop through the subfolders and split the images into train, val, and test sets
for subdir in os.listdir(data_folder):
    subdir_path = os.path.join(data_folder, subdir)
    if os.path.isdir(subdir_path):
        print("Processing folder:", subdir)
        # create subfolders in train, val, and test folders for the current subfolder
        train_subfolder = os.path.join(train_folder, subdir)
        val_subfolder = os.path.join(val_folder, subdir)
        test_subfolder = os.path.join(test_folder, subdir)
        os.makedirs(train_subfolder, exist_ok=True)
        os.makedirs(val_subfolder, exist_ok=True)
        os.makedirs(test_subfolder, exist_ok=True)
        # get a list of all the images in the subfolder
        images = [f for f in os.listdir(subdir_path) if os.path.isfile(os.path.join(subdir_path, f))]
        # shuffle the images randomly
        random.shuffle(images)
        # split the images into train, val, and test sets
        num_images = len(images)
        num_train = int(train_split * num_images)
        num_val = int(val_split * num_images)
        num_test = int(test_split * num_images)
        train_images = images[:num_train]
        val_images = images[num_train:num_train+num_val]
        test_images = images[num_train+num_val:num_train+num_val+num_test]
        # copy the images to the train, val, and test subfolders
        for image in train_images:
            src = os.path.join(subdir_path, image)
            dst = os.path.join(train_subfolder, image)
            shutil.copy(src, dst)
        for image in val_images:
            src = os.path.join(subdir_path, image)
            dst = os.path.join(val_subfolder, image)
            shutil.copy(src, dst)
        for image in test_images:
            src = os.path.join(subdir_path, image)
            dst = os.path.join(test_subfolder, image)
            shutil.copy(src, dst)

        print("done", subdir)    

import os
import cv2
import random
from shutil import copyfile

# Path to the directory containing the extracted UCF101 dataset
data_path = "D:/UCF101/UCF-101/"
# Path to the directory where the extracted frames will be stored
frames_path ="D:/UCF101/Frames/"

# Define the percentage split between train, test, and validation sets
train_pct = 0.7
test_pct = 0.2
val_pct = 0.1

# Create directories for train, test, and validation sets
train_path = os.path.join(frames_path, "train")
test_path = os.path.join(frames_path, "test")
val_path = os.path.join(frames_path, "validation")
os.makedirs(train_path, exist_ok=True)
os.makedirs(test_path, exist_ok=True)
os.makedirs(val_path, exist_ok=True)
# Iterate over the video files in the dataset directory and extract frames
# Loop through all folders and subfolders in data_path
# Iterate over the video files in the dataset directory and extract frames
# processed_folders = set()

# Iterate over the video files in the dataset directory and extract frames
for root, dirs, files in os.walk(data_path):
    # Skip the top-level directory as we only want to iterate over the subdirectories
    if root == data_path:
        continue
    for filename in files:
        if filename.endswith(".avi"):
            # Determine the label based on the directory name
            label = os.path.basename(root)
            # Open the video file using OpenCV
            video_path = os.path.join(root, filename)
            cap = cv2.VideoCapture(video_path)
            # Determine the total number of frames in the video
            num_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            # Iterate over each frame and extract it
            for i in range(num_frames):
                # Read the frame
                ret, frame = cap.read()
                if not ret:
                    break
                # Save the frame as an image file
                frame_filename = f"{os.path.splitext(filename)[0]}_{i}.jpg"
                frame_path = os.path.join(frames_path, label, frame_filename)
                os.makedirs(os.path.dirname(frame_path), exist_ok=True)
                cv2.imwrite(frame_path, frame)
            # Close the video file
            cap.release()


# Create a list of all the extracted frames
frames = []
for root, dirs, files in os.walk(frames_path):
    for filename in files:
        if filename.endswith(".jpg"):
            frames.append(os.path.join(root, filename))

# Shuffle the list of frames
random.shuffle(frames)

# Determine the number of frames in each set
num_frames = len(frames)
num_train = int(num_frames * train_pct)
num_test = int(num_frames * test_pct)
num_val = num_frames - num_train - num_test

# Split the list of frames into train, test, and validation sets
train_frames = frames[:num_train]
test_frames = frames[num_train:num_train+num_test]
val_frames = frames[num_train+num_test:]

# Copy the train frames to the train directory with labels
for frame_path in train_frames:
    label = os.path.basename(os.path.dirname(frame_path))
    frame_filename = os.path.basename(frame_path)
    train_label_path = os.path.join(train_path, label)
    os.makedirs(train_label_path, exist_ok=True)
    copyfile(frame_path, os.path.join(train_label_path, frame_filename))

# Copy the test frames to the test directory with labels
for frame_path in test_frames:
    label = os.path.basename(os.path.dirname(frame_path))
    frame_filename = os.path.basename(frame_path)
    test_label_path = os.path.join(test_path, label)
    os.makedirs(test_label_path, exist_ok=True)
    copyfile(frame_path, os.path.join(test_label_path, frame_filename))

# Copy the validation frames to the validation directory with labels
for frame_path in val_frames:
    label = os.path.basename(os.path.dirname(frame_path))
    frame_filename = os.path.basename(frame_path)
    val_label_path = os.path.join(val_path, label)
    os.makedirs(val_label_path, exist_ok=True)
    copyfile(frame_path, os.path.join(val_label_path, frame_filename))
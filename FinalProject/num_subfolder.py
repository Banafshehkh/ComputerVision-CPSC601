import os

def count_subfolders(data_path):
    count = 0
    for _, dirs, _ in os.walk(data_path):
        count += len(dirs)
    return count

data_path = "frames"
num_subfolders = count_subfolders(data_path)
print("Number of subfolders:", num_subfolders)

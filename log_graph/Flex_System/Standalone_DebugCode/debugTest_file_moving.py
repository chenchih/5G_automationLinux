import os
from pathlib import Path
path = 'C:\project'


# Specify the root directory to search
root_dir = "C:/Users/sam/Desktop/file1"

# Create an empty list to store the found text files
config_files = []

# Walk through the directory tree, starting from the root directory
for dirpath, _, files in os.walk(root_dir):
    for file in files:
        # Check if the file has a .txt extension
        if file.endswith(".txt"):
            # Construct the full path to the file
            full_path = os.path.join(dirpath, file)
            # Add the full path to the list of config files
            print(full_path)
            config_files.append(full_path)

# Now, `config_files` contains a list of full paths to all .txt files found
print(config_files)
#short code:
configfiles = [os.path.join(dirpath, f)
    for dirpath, dirnames, files in os.walk(path)
    for f in files if f.endswith('.txt')]

import fnmatch
for file in os.listdir():
    if fnmatch.fnmatchcase(file, "*.txt"):
        print(file)
    
#not txt file:
def filter_files(files, pattern):
    matched_files = [file for file in files if fnmatch.fnmatch(file, pattern)]
    return matched_files

# Example usage:
files = os.listdir('.')
txt_files = filter_files(files, "*.txt")
non_txt_files = [file for file in files if file not in txt_files]
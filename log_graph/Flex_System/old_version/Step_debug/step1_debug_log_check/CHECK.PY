import os, fnmatch
log_filename=""
filelist= '*.py' and '__pycache__'


# Define patterns to exclude
exclude_patterns = ['*.py', '__pycache__']
# List files in the current directory
listfiles = os.listdir()

# Filter files that do not match the exclude patterns
'''
matching_files = [
    file for file in listfiles 
    if not any(fnmatch.fnmatch(file, pattern) for pattern in exclude_patterns)
]
'''
matching_files = []
for file in listfiles:
    # Check if the file matches any of the exclude patterns
    exclude = False
    for pattern in exclude_patterns:
        print(f"Checking file '{file}' against pattern '{pattern}'")
        if fnmatch.fnmatch(file, pattern):
            exclude = True
            print(f"File '{file}' matches pattern '{pattern}', excluding.")
            break  # No need to check other patterns, skip this file
    if not exclude:
        matching_files.append(file)  # Add to matching_files if not excluded



#print(f"List File current directory:\n{chr(10).join(matching_files)}")

import os
#import datetime
from datetime import datetime
import shu

filename = input('Enter your filename: ')

# 2. Create the datetime folder
now = datetime.datetime.now()
folder_name = now.strftime("%Y-%m-%d_%H-%M-%S")  # Format: YYYY-MM-DD_HH-MM-SS
os.makedirs(folder_name, exist_ok=True)  # Create folder, no error if it exists
print(f"Folder '{folder_name}' created.")

 # 3. Move the file into the folder
destination_path = os.path.join(folder_name, filename)
shutil.move(filename, destination_path)
print(f"File '{filename}' moved to '{destination_path}'.")






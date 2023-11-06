import os
import re

# Define the path to the directory containing the files
folder_path = './spectra'  # Change to your folder path

# Regular expression to match filenames and capture the desired part
pattern = r'.*?_.*?_(?P<filename>[^_]+\.\w+\.\w+)'

for file_name in os.listdir(folder_path):
    # Check if the file is a .tif or .txt file
    if file_name.endswith('.tif') or file_name.endswith('.txt'):
        match = re.match(pattern, file_name)
        if match:
            # Extract the desired part of the filename
            new_file_name = match.group('filename')
            # Construct the full old and new paths
            old_path = os.path.join(folder_path, file_name)
            new_path = os.path.join(folder_path, new_file_name)
            # Rename the file
            os.rename(old_path, new_path)
            print(f'Renamed {file_name} to {new_file_name}')


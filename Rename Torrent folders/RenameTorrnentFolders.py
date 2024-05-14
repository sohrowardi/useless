import os
import re

# Get the current directory where the script is located
base_directory = os.path.dirname(os.path.abspath(__file__))

# Function to clean up folder names
def clean_folder_name(folder_name):
    # Remove content within square brackets
    folder_name = re.sub(r'\[.*?\]', '', folder_name)
    # Remove leading and trailing whitespace
    folder_name = folder_name.strip()
    return folder_name

# Iterate through the folders and rename them
for folder_name in os.listdir(base_directory):
    if os.path.isdir(os.path.join(base_directory, folder_name)):
        new_folder_name = clean_folder_name(folder_name)
        os.rename(os.path.join(base_directory, folder_name), os.path.join(base_directory, new_folder_name))

print("Folders renamed successfully.")

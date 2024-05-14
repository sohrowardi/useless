import os
from datetime import datetime

def create_and_rename_folder():
    folder_title = input("Enter folder title: ")
    current_date = datetime.now().strftime("%y.%m.%d")
    new_folder_name = f"{current_date} - {folder_title}"
    
    # Get the current directory
    current_directory = os.getcwd()

    # Create a new folder
    new_folder_path = os.path.join(current_directory, new_folder_name)
    os.mkdir(new_folder_path)

    print(f"Folder '{new_folder_name}' created successfully.")

if __name__ == "__main__":
    create_and_rename_folder()

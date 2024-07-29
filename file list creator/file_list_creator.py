import os
import tkinter as tk
from tkinter import filedialog

def create_txt_file(folder_path, selected_extension, with_extension):
    # Get the folder name
    folder_name = os.path.basename(folder_path)
    
    # Create a txt file with the folder name
    with open(folder_name + ".txt", "w", encoding="utf-8") as txt_file:
        # List all files in the folder
        files = os.listdir(folder_path)
        # Write file names to the txt file
        for file in files:
            if file.endswith(selected_extension):
                if with_extension:
                    txt_file.write(file + "\n")
                else:
                    file_name = os.path.splitext(file)[0] # Extract filename without extension
                    txt_file.write(file_name + "\n")
                print("Writing:", file)  # Print progression to the terminal


def select_folder():
    root = tk.Tk()
    root.withdraw() # Hide the root window

    # Ask user for the extension type
    extension = input("Enter the extension type you want to select (e.g., .mp4, .mp3, .wav): ")
    # Ask user if they want to write filenames with extensions
    with_extension = input("Do you want to write file names with extensions? (yes/no): ").lower() == 'yes'

    folder_selected = filedialog.askdirectory(title="Select a folder")
    if folder_selected:
        if os.path.isdir(folder_selected):
            create_txt_file(folder_selected, extension, with_extension)
            print("Text file created successfully.")
        else:
            print("Invalid folder selected.")
    else:
        print("No folder selected.")

if __name__ == "__main__":
    select_folder()

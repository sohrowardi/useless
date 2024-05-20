import os
import subprocess
import pyperclip
from tkinter import filedialog
import tkinter as tk

def write_folder_structure(folder_path, output_file):
    """
    Write the folder structure and contents to a text file.

    Parameters:
        folder_path (str): The path of the folder to analyze.
        output_file (str): The path of the output text file.

    Returns:
        None
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        for root, dirs, files in os.walk(folder_path):
            # Ignore specified folders and their contents
            if '_github' in dirs:
                dirs.remove('_github')
            if '.git' in dirs:
                dirs.remove('.git')
            if ".venv" in dirs:
                dirs.remove('.venv')
            if "__pycache__" in dirs:
                dirs.remove('__pycache__')
                continue  # Skip traversing into .git folder

            indent_level = root.count(os.sep) - folder_path.count(os.sep)
            folder_name = os.path.basename(root)
            f.write('    ' * indent_level + folder_name + '\n')
            print('    ' * indent_level + folder_name)  # Print folder name to terminal
            sub_indent = '    ' * (indent_level + 1)
            for file in files:
                if not file.endswith('.txt'):  # New condition here
                    f.write(sub_indent + '├── ' + file + '\n')
                    print(sub_indent + '├── ' + file)  # Print file name to terminal
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, 'r', encoding='utf-8') as infile:
                            content = infile.read()
                            f.write(sub_indent + '|   ' + content.strip().replace('\n', '\n' + sub_indent + '|   ') + '\n')
                            print(sub_indent + '|   ' + content.strip().replace('\n', '\n' + sub_indent + '|   '))  # Print file content to terminal
                    except UnicodeDecodeError:
                        print(f"UnicodeDecodeError: Skipping file '{file_path}'")

def open_and_copy_file(file_path):
    """
    Open a file and copy its content to the clipboard.

    Parameters:
        file_path (str): The path of the file to open and copy.

    Returns:
        None
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        pyperclip.copy(content)

def select_folder():
    """
    Prompt the user to select a folder.

    Returns:
        str: The path of the selected folder.
    """
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    folder_path = filedialog.askdirectory(title="Select a folder to analyze")
    return folder_path

if __name__ == "__main__":
    selected_folder = select_folder()
    if selected_folder:
        # Get the directory where the Python script is located
        script_directory = os.path.dirname(__file__)
        # Ensure the "txt" subfolder exists in the script directory
        txt_folder = os.path.join(script_directory, "txt")
        if not os.path.exists(txt_folder):
            os.makedirs(txt_folder)

        output_file = os.path.join(txt_folder, f"{os.path.basename(selected_folder)}.txt")
        write_folder_structure(selected_folder, output_file)
        print("Folder structure and contents written to", output_file)
        # Add input prompt to prevent the terminal from closing immediately
        input("Press Enter to open the file in Notepad and copy its content to clipboard...")
        # Open the file in Notepad
        subprocess.Popen(["notepad.exe", output_file])
        # Copy file content to clipboard
        open_and_copy_file(output_file)
        print("Contents copied to clipboard.")
    else:
        print("No folder selected.")

# File List Creator

## Overview
The File List Creator is a Python utility that generates a text file listing all files within a selected directory that match a specified file extension. It offers the option to include or exclude file extensions in the generated list.

## Features
- **Interactive GUI**: Utilizes a graphical interface to select the target folder.
- **Custom Extension Selection**: Allows users to specify the type of file extension to filter.
- **Extension Inclusion Option**: Users can choose whether to include the file extension in the output list.
- **Progress Display**: Prints the progress to the terminal as files are written to the text file.

## Requirements
- Python 3.x
- Tkinter library (usually included with Python)

## Usage
1. Run the `file_list_creator.py` script.
2. Enter the desired file extension when prompted (e.g., `.mp4`, `.mp3`, `.wav`).
3. Specify whether to include file extensions in the filenames (`yes` or `no`).
4. Select the target folder using the file dialog.
5. A text file named after the folder will be created, listing all files with the chosen extension.

## How It Works
The script uses the `os` and `tkinter` libraries to interact with the file system and the user interface. When executed, it prompts the user for input, processes the selected directory, and outputs a text file with the list of filenames.

## Contributing
Contributions to the File List Creator are welcome. Please ensure to update tests as appropriate.
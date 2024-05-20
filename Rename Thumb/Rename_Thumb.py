import os
import re

def rename_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".png"):
            # Extract the movie name from the filename
            movie_name = re.search(r'(.+?)(\d{4}-\d{2}-\d{2}-\d{2}h\d{2}m\d{2}s\d{3})', filename).group(1)
            
            # Remove the file extension from the movie name
            movie_name = os.path.splitext(movie_name)[0]
            
            # Count the number of files with the same movie name
            same_movie_files = [file for file in os.listdir(directory) if file.startswith(movie_name)]
            file_number = same_movie_files.index(filename) + 1
            
            # Create the new filename
            new_filename = f"{movie_name} ({file_number}).png"
            
            # Rename the file
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))

rename_files(os.getcwd())

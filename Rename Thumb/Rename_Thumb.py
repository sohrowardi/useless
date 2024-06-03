import os
import re

def rename_files(directory):
    for root, dirs, files in os.walk(directory):
        movie_files = {}  # Dictionary to keep track of counts for each movie name

        for filename in files:
            if filename.endswith(".png"):
                match = re.search(r'(.+?)(\d{4}-\d{2}-\d{2}-\d{2}h\d{2}m\d{2}s\d{3})', filename)
                if match:
                    movie_name = match.group(1).strip()

                    # Update the count for the movie name
                    if movie_name not in movie_files:
                        movie_files[movie_name] = 0
                    movie_files[movie_name] += 1
                    file_number = movie_files[movie_name]

                    # Create the new filename
                    new_filename = f"{movie_name} ({file_number}).png"

                    # Rename the file
                    os.rename(os.path.join(root, filename), os.path.join(root, new_filename))

rename_files(os.getcwd())

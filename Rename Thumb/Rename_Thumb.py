import os
import re

def rename_files(directory):
    movie_files = {}  # Dictionary to keep track of counts for each movie name

    for root, dirs, files in os.walk(directory):
        # First, count existing formatted files
        for filename in files:
            formatted_match = re.match(r'(.+?) \((\d+)\)\.png', filename)
            if formatted_match:
                movie_name = formatted_match.group(1).strip()
                file_number = int(formatted_match.group(2))

                if movie_name not in movie_files:
                    movie_files[movie_name] = file_number
                else:
                    movie_files[movie_name] = max(movie_files[movie_name], file_number)

        # Now, rename files with timestamps
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
                    old_file_path = os.path.join(root, filename)
                    new_file_path = os.path.join(root, new_filename)

                    # Ensure the new filename does not conflict with an existing file
                    while os.path.exists(new_file_path):
                        movie_files[movie_name] += 1
                        file_number = movie_files[movie_name]
                        new_filename = f"{movie_name} ({file_number}).png"
                        new_file_path = os.path.join(root, new_filename)

                    os.rename(old_file_path, new_file_path)

rename_files(os.getcwd())

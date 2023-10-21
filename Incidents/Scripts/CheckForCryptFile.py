import os
import re

# Define the directory to start the search (e.g., root directory)
start_directory = "/"  # Change this to the directory where you want to start the search

# Regular expression pattern
pattern = re.compile(".*\.txt.[a-zA-Z0-9]{10}.1")  # Change this to your desired regex pattern

# Function to search for files matching the pattern
def search_files_in_directory(directory, pattern):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if re.match(pattern, file):
                print("File Path:", file_path)
                #fileExtension = file_path.split("/")
                #file = fileExtension[-1]
                #file.match(file, pattern)

# Start the search
search_files_in_directory(start_directory, pattern)


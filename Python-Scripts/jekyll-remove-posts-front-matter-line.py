"""
A script for removing the first line of code that start with a specific text, 
useful for removing Jekyll front matter lines.

- It walks recursively through the given directory `DIR` and its subdirectories.
- Looks for files with a date prefix in the format "YYYY-MM-DD".
- In each file, it deletes the first line it finds starting with`PREFIX`.

Python 3.11.8
"""

import os
import re
import logging
import tempfile
import shutil

DIR = "/path/to/directory/_posts"
PREFIX = "categories:"

def log_config():
    """performs a logging basic setup"""
    handler_to_file = logging.FileHandler("log.log", "w")
    handler_to_file.setLevel(logging.DEBUG)
    handler_to_console = logging.StreamHandler()
    handler_to_console.setLevel(logging.ERROR)
    logging.basicConfig(
        handlers=[
            handler_to_file,
            handler_to_console,
        ],
        format="%(asctime)s: %(levelname)s %(filename)s %(lineno)s: %(message)s",
        level=logging.DEBUG,
    )

def is_text_file(filepath):
    """Check if a file is a text file."""
    try:
        with open(filepath, 'tr') as check_file:  # open in text mode to read
            check_file.read(1024)  # Read the first 1024 bytes
        logging.debug(f"file is readable: {filepath}")
        return True
    except:  # If an error occurs, it's likely not a text file.
        logging.error(f"File is NOT readable: {filepath}")
        return False

def delete_first_line_starting_with(file_path, prefix):
    # Create a temporary file
    temp_fd, temp_path = tempfile.mkstemp()
    with os.fdopen(temp_fd, 'w', encoding='utf-8') as temp_file:
        with open(file_path, 'r', encoding='utf-8') as f:
            line_already_skipped = False
            for line in f:
                if line_already_skipped:
                    temp_file.write(line)
                elif not line.startswith(prefix):
                    temp_file.write(line)
                elif line.startswith(prefix):
                    line_already_skipped = True
    
    # Replace the original file with the temporary file
    os.remove(file_path)
    shutil.copy(temp_path, file_path) 



def process_directory(root_dir, search_text):
    """Walk through the directory and its subdirectories to find and replace text in files."""
    for root, dirs, files in os.walk(root_dir):
        for filename in files:
            if re.match(r'\d{4}-\d{2}-\d{2}', filename) and is_text_file(os.path.join(root, filename)):
                logging.debug(f"file found: '{filename}'")
                delete_first_line_starting_with(os.path.join(root, filename), search_text)
            else:
                logging.debug(f"file doesn't match pattern: '{filename}'")

if __name__ == "__main__":
    log_config()
    logging.debug("script started")
    directory_path = DIR
    search_text = PREFIX
    
    process_directory(directory_path, search_text)

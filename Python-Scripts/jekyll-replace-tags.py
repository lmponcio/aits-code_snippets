"""
A script for finding and replacing text, useful for changing Jekyll tags:
- It walks recursively through the given directory `DIR` and its subdirectories.
- Looks for files with a date prefix in the format "YYYY-MM-DD".
- Performs a find and replace operation within these files
- Replaces all occurrences of `SEARCH_STRING` with `REPLACE_STRING`.

Python 3.11.8
"""

import os
import re
import logging

DIR = "/path/to/directory/_posts"
SEARCH_STRING = "post_url "
REPLACE_STRING = "post_url_short "

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
        logging.debug(f"File is readable: {filepath}")
        return True
    except:  # If an error occurs, it's likely not a text file.
        logging.error(f"File is NOT readable: {filepath}")
        return False

def replace_in_file(file_path, search_text, replacement_text):
    """Replace text in a file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        file_contents = file.read()
    
    file_contents = file_contents.replace(search_text, replacement_text)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(file_contents)
    logging.debug(f"Replaced text '{search_text}' for '{replacement_text}' in file{file_path}")



def process_directory(root_dir, search_text, replacement_text):
    """Walk through the directory and its subdirectories to find and replace text in files."""
    for root, dirs, files in os.walk(root_dir):
        for filename in files:
            if re.match(r'\d{4}-\d{2}-\d{2}', filename) and is_text_file(os.path.join(root, filename)):
                logging.debug(f"file found: '{filename}'")
                replace_in_file(os.path.join(root, filename), search_text, replacement_text)
            else:
                logging.debug(f"file doesn't match pattern: '{filename}'")

if __name__ == "__main__":
    log_config()
    logging.debug("script started")
    directory_path = DIR
    search_text = SEARCH_STRING
    replacement_text = REPLACE_STRING
    
    process_directory(directory_path, search_text, replacement_text)

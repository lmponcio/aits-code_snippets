#!/bin/bash

API_DIR="/path/to/api/project/dir"
SITE_DIR="/path/to/site/project"

# opening the API in vscode and running the the API in a new terminal 
code "$API_DIR"
gnome-terminal --working-directory="$API_DIR" -- bash -c "
    source '$API_DIR/.venv/bin/activate';
    python '$API_DIR/main.py';
    exec bash
"

# opening the Site in vscode,running the Site in a new terminal, and opening it in firefox
code "$SITE_DIR"
gnome-terminal --working-directory="$SITE_DIR" -- bash -c "
    docker start containername -i;
    exec bash
"
sleep 5 # waiting for 5 seconds untill the site is running
firefox http://0.0.0.0:8080/

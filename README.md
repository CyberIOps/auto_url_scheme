# URL Scheme Completer

This script processes a list of paths from a text file and generates complete URLs by appending a specified domain and scheme (`http`). The resulting URLs are saved in an output file.

* [scheme][domain][tld]/URL

## Features

- Reads a list of paths from an input file.
- Appends the specified domain and `http` scheme to each path.
- Saves the generated URLs to an output file.
- Handles empty lines gracefully.

## Requirements

- Python 3.x
- Basic understanding of file handling in Python.

## How to Use

1. Prepare an input text file with the list of paths, one path per line (e.g., `doms.txt`).
2. Place the script in the same directory as your input file.
3. Run the script in a Python environment or terminal.

### Running the Script

1. Clone this repository or download the script.
2. Open a terminal or command prompt.
3. Run the script with:
   ```bash
   python script_name.py

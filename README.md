# Folder Structure Analysis Script

## Project Description

This repository contains a Python script that analyzes a manually created folder structure.

The folder includes:
- Two `.txt` files directly inside the main folder.
- Two subfolders:
  - One empty subfolder.
  - One subfolder containing two `.txt` files.

The Python script performs the following:
- Counts how many files or folders are in the main folder (not including contents of subfolders).
- Prints the name of any empty subfolders.
- Prints the name of any non-empty subfolders and the number of files inside them.

## Folder Structure

folder-task/
├── file1.txt
├── file2.txt
├── Folder1/
└── TextFolder/
    ├── abc.txt
    └── xyz.txt

> Note: The folder and files were created manually as per the instructions. `Folder1` is intentionally empty, and `TextFolder` contains two `.txt` files.

## How to Run

1. Clone this repository:
   git clone https://github.com/yourusername/Task_RA.git

2. Navigate to the folder:
   cd Task_RA

3. Run the Python script:
   python analyze_structure.py
   (or)
   py analyze_structure.py

## Example Output

Total files/folders in main folder: 8
Non-empty subfolder '.git' has 5 file(s)
Non-empty subfolder 'Folder1' has 1 file(s)
Non-empty subfolder 'TextFolder' has 2 file(s)

The script works regardless of:
- The number of files in the main folder.
- The number of files in subfolders.
- Where the script is located on your system.

##

- Python 3.6 or above
- No external packages are required

## 🧑‍💻 Author

Your Name  
your.email@example.com

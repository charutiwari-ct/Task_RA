import os

# Folder where script is located
main_folder = os.path.abspath(os.path.dirname(__file__))

# List all files and folders directly in main folder
entries = os.listdir(main_folder)
top_level = [e for e in entries if os.path.isfile(os.path.join(main_folder, e)) or os.path.isdir(os.path.join(main_folder, e))]
print(f"\nTotal files/folders directly in main folder: {len(top_level)}")

# Check each folder
for entry in entries:
    path = os.path.join(main_folder, entry)
    if os.path.isdir(path):
        contents = os.listdir(path)
        if not contents:
            print(f"Empty subfolder: {entry}")
        else:
            file_count = len([f for f in contents if os.path.isfile(os.path.join(path, f))])
            print(f"Non-empty subfolder '{entry}' has {file_count} file(s)")

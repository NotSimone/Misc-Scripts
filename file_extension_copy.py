# Copies all files of an extension type from subfolders into a new folder
# Renames based on the name of the parent folder

import os, shutil
path = "."
dest_folder = os.path.join(path, "files")
extension = [".jpg"]

# If true, renames the files based on the parent folder name
FOLDER_RENAME = True

# Checks all files in directory and subdirectories recursively for extension
def check_folder(file_path):
    # Create dest folder
    os.makedirs(dest_folder, exist_ok=True)

    file_list = os.listdir(file_path)

    counter = 0
    for file in file_list:
        # Create full path
        full_path = os.path.join(file_path, file)
        # Check if it is a file or directory and make recursive calls
        if (os.path.isdir(full_path)):
            # Don't recurse into output folder
            if (full_path != dest_folder):
                check_folder(full_path)
        else:
            _, file_ext = os.path.splitext(full_path)
            if (file_ext in extension):
                # Generate new file name and copy
                test = os.path.basename(os.path.dirname(full_path))
                if FOLDER_RENAME:
                    output_path = os.path.join(dest_folder, test + "_" + str(counter) + file_ext)
                    counter += 1
                else:
                    output_path = os.path.join(dest_folder, os.path.basename(full_path))
                shutil.copy(full_path, output_path)

# Initial function call on path
check_folder(path)

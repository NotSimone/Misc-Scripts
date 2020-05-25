# Removes all files in subdirectories without given file ext

import os

# Get confirmation
def yes_or_no(question):
    reply = str(input(question+' (y/n): ')).lower().strip()
    if reply[0] == 'y':
        return True
    if reply[0] == 'n':
        return False
    else:
        return yes_or_no("Uhhhh... please enter ")

path = "."
extension = [".py", ".epub", ".cbz"]

file_keep = []
file_delete = []

# Checks all files in directory and subdirectories recursively for extension
def check_folder(file_path):
    file_list = os.listdir(file_path)
    for file in file_list:
        # Create full path
        full_path = os.path.join(file_path, file)
        # Check if it is a file or directory and make recursive calls
        if (os.path.isdir(full_path)):
            check_folder(full_path)
        else:
            _, file_ext = os.path.splitext(full_path)
            if (file_ext in extension):
                global file_keep
                file_keep.append(full_path)
            else:
                global file_delete
                file_delete.append(full_path)

# Initial function call on path
check_folder(path)

# Print file lists
print("Deleting:")
for x in file_delete:
    print(x)

# Get confirmation
if yes_or_no('Do you want to continue?'):
    for x in file_delete:
        os.remove(os.path.abspath(x))
    print("Done")

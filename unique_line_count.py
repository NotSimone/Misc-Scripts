# Counts the number of unique/duplicate lines in a text file

import argparse

# Parse argument
parser = argparse.ArgumentParser()
parser.add_argument("file_arg")
file_location = parser.parse_args().file_arg

# Open the file
with open(file_location, "r") as file:
    # Add lines to the appropriate lists
    unique_list = list()
    dupe_list = list()
    for line in file:
        # Remove newline
        line = line.rstrip("\n")
        if len(line) > 0 and line not in unique_list:
            unique_list.append(line)
        else:
            dupe_list.append(line)

# Print out results
print("== Unique Lines ==")
for x in unique_list:
    print(x)

print("== Duplicate Lines ==")
for x in dupe_list:
    print(x)


print(f"Number of unique lines: {len(unique_list)}")
print(f"Number of duplicate lines: {len(dupe_list)}")
print(f"Total lines: {len(unique_list) + len(dupe_list)}")

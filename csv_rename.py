# Renames files based on a csv file

# First column should be the source name
# Second column should be the dest name
# Prefixes and postfixes for file names specified below

# Also pads source numbers to be double digits

import os, csv

rename_dict = {}

# Padding for file names
source_prefix = "IMG_00"
source_postfix = ".JPG"
dest_prefix = ""
dest_postfix = ".JPG"

# Read the csv file into a dictionary
with open("input.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data = list(row.items())
        # Store, ignoring empty
        if (not data[1][1]):
            continue
        # Pad 0 in front for single digit numbers
        if (int(data[0][1])) < 10:
            rename_dict["0" + data[0][1]] = data[1][1]
        else:
            rename_dict[data[0][1]] = data[1][1]

print(rename_dict)

# Rename files
for x in rename_dict:
    source_file = source_prefix + x + source_postfix
    dest_file = dest_prefix + rename_dict[x] + dest_postfix
    try:
        os.rename(source_file, dest_file)
        print("Renamed: " + dest_file)
    except(FileNotFoundError):
        print("Could not find file: " + source_file + " - Skipping")

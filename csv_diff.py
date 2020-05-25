# Finds difference between two CSV files

# First arg is first file, second is second file
# Stops when either CSV runs out of rows
# Prints the column name in optional arg --col in differences

import argparse, csv

# Parse file location
parser = argparse.ArgumentParser()
parser.add_argument("file_1_arg")
parser.add_argument("file_2_arg")
parser.add_argument("--col")
file_1_location = parser.parse_args().file_1_arg
file_2_location = parser.parse_args().file_2_arg
display_column = parser.parse_args().col

with open(file_1_location, mode="r", encoding="utf-8-sig") as csv_1_file:
    with open(file_2_location, mode="r", encoding="utf-8-sig") as csv_2_file:
        # Grab dictionary iterable for both csvs
        csv_1_reader = csv.DictReader(csv_1_file)
        csv_2_reader = csv.DictReader(csv_2_file)
        # Merge the two iterables into an iterable of tuples
        csv_tuple = zip(csv_1_reader, csv_2_reader)
        row = 0
        count = 0
        for pair in csv_tuple:
            # Check that the keys are okay
            if pair[0].keys() != pair[1].keys():
                raise Exception("Error: Column do not match")
            if display_column not in pair[0].keys():
                raise Exception("Error: Specified display column not a csv column")
            # Dictionary comprehension to make a dictionary of differences per row
            diff_dict_1 = {k: pair[0][k] for k in pair[0].keys() if pair[0][k] != pair[1][k]}
            diff_dict_2 = {k: pair[1][k] for k in pair[0].keys() if pair[0][k] != pair[1][k]}
            if diff_dict_1:
                print(f"[{row}] ({pair[0][display_column]}) {diff_dict_1} -> {diff_dict_2}")
                count += 1
            row += 1
        # Print stats
        print(f"Found {count} different rows in {row} total rows")

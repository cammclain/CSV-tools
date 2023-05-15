import os
import sys
import csv

# Function to create a directory if it doesn't exist
def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# Function to write rows to a CSV file
def write_rows_to_csv(filename, rows):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(rows)

# Function to split a large CSV file into smaller files and organize them into directories
def split_csv_file(input_file, output_directory):
    # Read the input CSV file
    with open(input_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)

    # Create directories for different row counts
    create_directory(output_directory)
    directories = {
        1: os.path.join(output_directory, '1_row'),
        2: os.path.join(output_directory, '2_rows'),
        3: os.path.join(output_directory, '3_rows'),
        5: os.path.join(output_directory, '5_rows'),
        10: os.path.join(output_directory, '10_rows'),
        15: os.path.join(output_directory, '15_rows'),
        20: os.path.join(output_directory, '20_rows'),
        25: os.path.join(output_directory, '25_rows'),
        50: os.path.join(output_directory, '50_rows'),
        75: os.path.join(output_directory, '75_rows'),
        100: os.path.join(output_directory, '100_rows'),
        150: os.path.join(output_directory, '150_rows')
    }
    for directory in directories.values():
        create_directory(directory)

    # Split rows into smaller groups and write to respective CSV files
    for count, directory in directories.items():
        for i in range(0, len(rows), count):
            output_filename = os.path.join(directory, f'file_{i // count}.csv')
            write_rows_to_csv(output_filename, rows[i:i+count])

# Check if the correct number of arguments is provided
if len(sys.argv) != 3:
    print('Usage: python script.py input_file output_directory')
else:
    # Retrieve the input file path and output directory name from command-line arguments
    input_file = sys.argv[1]
    output_directory = sys.argv[2]

    # Call the function to split the CSV file
    split_csv_file(input_file, output_directory)

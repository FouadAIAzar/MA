import csv

def check_csv_file(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        row_lengths = set()
        for i, row in enumerate(reader, 1):
            row_lengths.add(len(row))
            if len(row_lengths) > 1:
                print(f"Row {i} has a different length! Lengths encountered so far: {row_lengths}")
                return False
        print("All rows have consistent lengths.")
        return True

filename = "train.csv"
check_csv_file(filename)


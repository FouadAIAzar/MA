import os
import csv

def count_rows_in_csv(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        return sum(1 for row in reader)

def main():
    directory = 'adjusted_spectra'
    row_counts = []

    # Ensure the directory exists
    if not os.path.exists(directory):
        print(f"'{directory}' directory does not exist.")
        return

    # Get list of all CSV files in the directory
    csv_files = [f for f in os.listdir(directory) if f.endswith('.csv')]

    if not csv_files:
        print("No CSV files found in the directory.")
        return

    # Count rows in each CSV file and store in row_counts list
    for csv_file in csv_files:
        full_path = os.path.join(directory, csv_file)
        row_counts.append(count_rows_in_csv(full_path))

    # Check if all counts are the same
    if len(set(row_counts)) == 1:
        print("All CSV files have the same number of rows.")
    else:
        print("Not all CSV files have the same number of rows.")
        for csv_file, count in zip(csv_files, row_counts):
            print(f"{csv_file}: {count} rows")

if __name__ == "__main__":
    main()


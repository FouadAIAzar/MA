import csv
from collections import defaultdict

def identify_datatype(value):
    try:
        int(value)
        return "int"
    except ValueError:
        pass

    try:
        float(value)
        return "float"
    except ValueError:
        pass

    return "string"

def analyze_column_datatypes(filename, column_index):
    data_type_freq = defaultdict(int)

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # skip header if present

        for row in reader:
            if column_index < len(row):  # Ensure column index is within bounds
                value = row[column_index]
                datatype = identify_datatype(value)
                data_type_freq[datatype] += 1
            else:
                print(f"Row {reader.line_num} has fewer than {column_index + 1} columns.")

    return data_type_freq

filename = "descriptors.csv"
column_index = 1

freqs = analyze_column_datatypes(filename, column_index)
for datatype, count in freqs.items():
    print(f"{datatype}: {count} occurrences")



import csv

# Open the backup CSV file for reading
with open("descriptors_backup.csv", "r") as infile:
    reader = csv.reader(infile)
    
    # Extract the header and the rows that don't have "0" in the first column
    rows = [row for row in reader if row[0] != "0"]

# Open the desired output file for writing
with open("descriptors.csv", "w", newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(rows)

print("Filtered CSV saved to descriptors.csv!")


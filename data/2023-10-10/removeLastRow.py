import csv

# Open the CSV file for reading
with open("descriptors.csv", "r") as infile:
    reader = csv.reader(infile)
    rows = list(reader)

# Remove the last row
rows.pop()

# Open the CSV file for writing (overwrite mode)
with open("descriptors.csv", "w", newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(rows)

print("Last row removed from descriptors.csv!")


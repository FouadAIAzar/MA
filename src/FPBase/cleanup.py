import csv

# Read the CSV and process rows
updated_rows = []
with open("proteins_info.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Check and update cells with only "[]" value
        for key, value in row.items():
            if value == "[]":
                row[key] = ""
        updated_rows.append(row)

# Write the updated data back to the CSV
with open("proteins_info.csv", "w", newline='') as csvfile:
    fieldnames = reader.fieldnames  # Using fieldnames from the original reader
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in updated_rows:
        writer.writerow(row)


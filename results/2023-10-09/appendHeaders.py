import csv

# Open and read the headers csv file
with open('headersSanitized.csv', 'r') as headers_file:
    headers = list(csv.reader(headers_file))[0]

# Open and read the descriptors backup csv file
with open('descriptors_backup.csv', 'r') as descriptors_backup_file:
    descriptors_backup = list(csv.reader(descriptors_backup_file))

# Combine headers and descriptors
combined = [headers] + descriptors_backup

# Write the combined list back to the descriptors backup csv file
with open('descriptors_backup.csv', 'w', newline='') as combined_file:
    writer = csv.writer(combined_file)
    writer.writerows(combined)


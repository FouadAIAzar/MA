import os
import csv

# Directory containing the substance folders
substances_directory = './substances'

# File to store the catalogue information
catalogue_csv_path = './catalogue.csv'

# Initialize a list to hold the catalogue data
catalogue_data = []

# Process each folder in the substances directory
for folder in os.listdir(substances_directory):
    folder_path = os.path.join(substances_directory, folder)
    
    if os.path.isdir(folder_path):
        # Initialize record with folder name
        record = {'name': folder, 'cid': '', 'em': False, 'ab': False, 'ex': False}

        # Read the CID from the text file
        cid_file_path = os.path.join(folder_path, f'{folder}_CID.txt')
        if os.path.exists(cid_file_path):
            with open(cid_file_path, 'r') as cid_file:
                cid_content = cid_file.read().strip()
                # Remove the first 5 characters
                record['cid'] = cid_content[5:] if len(cid_content) > 5 else ""

        # Check for the existence of EM.csv, AB.csv, and EX.csv
        record['em'] = os.path.exists(os.path.join(folder_path, 'EM.csv'))
        record['ab'] = os.path.exists(os.path.join(folder_path, 'AB.csv'))
        record['ex'] = os.path.exists(os.path.join(folder_path, 'EX.csv'))

        # Add the record to the catalogue data
        catalogue_data.append(record)

# Write the catalogue data to a CSV file
with open(catalogue_csv_path, 'w', newline='') as csvfile:
    fieldnames = ['name', 'cid', 'em', 'ab', 'ex']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for row in catalogue_data:
        writer.writerow(row)

print("Catalogue creation complete.")

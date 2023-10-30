import csv

# Open the CSV file and read its contents
with open('proteins_info.csv', 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    with open('proteins.fasta', 'w') as fasta_file:
        for row in reader:
            # Get the id and seq from the row
            _id = row['id']
            seq = row['seq']
            
            # Compile the id and seq into the FASTA format
            fasta_entry = f">{_id}\n{seq}\n"
            
            # Write the FASTA entry to the output file
            fasta_file.write(fasta_entry)


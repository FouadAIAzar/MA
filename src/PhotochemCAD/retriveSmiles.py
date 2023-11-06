import csv
import requests

# Define a function to get SMILES from PubChem
def get_smiles_from_pubchem(compound_name):
    base_url = "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name"
    url = f"{base_url}/{compound_name}/property/CanonicalSMILES/TXT"
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        return response.text.strip()
    else:
        print(f"Error retrieving SMILES for {compound_name}")
        return None

# Read the TSV file and fetch SMILES for each compound
with open('list.tsv', 'r') as infile, open('output.tsv', 'w', newline='') as outfile:
    reader = csv.DictReader(infile, delimiter='\t')
    fieldnames = reader.fieldnames + ['SMILES']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames, delimiter='\t')
    
    writer.writeheader()
    
    for row in reader:
        compound_name = row['name']
        smiles = get_smiles_from_pubchem(compound_name)
        if smiles:
            row['SMILES'] = smiles
            writer.writerow(row)

print("Finished retrieving SMILES.")


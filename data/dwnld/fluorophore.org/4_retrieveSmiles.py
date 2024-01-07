import pandas as pd
import requests

def get_smiles_from_pubchem(cas_number):
    # PubChem API endpoint for searching by CAS number
    url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{cas_number}/property/CanonicalSMILES/JSON"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            # Extract the SMILES string
            smiles = data['PropertyTable']['Properties'][0]['CanonicalSMILES']
            return smiles
        else:
            print(f"Failed to retrieve data for CAS: {cas_number}")
            return None
    except Exception as e:
        print(f"Error occurred for CAS: {cas_number}: {e}")
        return None

# Read the filtered CSV file
df = pd.read_csv('filtered_catalogue.csv')

# Retrieve SMILES for each CAS number and store in a new column
df['SMILES'] = df['CAS Number'].apply(get_smiles_from_pubchem)

# Save the updated DataFrame to a new CSV file
df.to_csv('catalogue_with_smiles.csv', index=False)

print("Data updated with SMILES. New CSV file saved as 'catalogue_with_smiles.csv'.")

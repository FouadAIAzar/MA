import pandas as pd
import pubchempy as pcp

# Function to get SMILES from CID
def get_smiles(cid):
    try:
        compound = pcp.Compound.from_cid(cid)
        return compound.isomeric_smiles
    except Exception:
        return None

# Load the catalogue.csv with CID as string
try:
    df = pd.read_csv('catalogue.csv', encoding='utf-8', dtype={'cid': str})
except UnicodeDecodeError:
    df = pd.read_csv('catalogue.csv', encoding='ISO-8859-1', dtype={'cid': str})

# Apply the function to each CID
df['smiles'] = df['cid'].apply(lambda x: get_smiles(x) if pd.notna(x) and x != "" else None)

# Save the updated dataframe with utf-8 encoding
df.to_csv('catalogue.csv', index=False, encoding='utf-8')

print("SMILES retrieval and catalogue update complete.")

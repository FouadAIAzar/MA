import pandas as pd
from rdkit import Chem
from rdkit.Chem import Draw

# Read the CSV file containing smiles
df = pd.read_csv('molecules.csv')

# Iterate over the smiles and generate PNG images
for i, row in df.iterrows():
    smiles = row['Chromophore']
    tag = row['Tag']
    molecule = Chem.MolFromSmiles(smiles)
    if molecule is not None:
        
        # Generate the image
        img = Draw.MolToImage(molecule)
        # Save the image
        img.save(f'./images/smile_{tag}.png')
        print(tag)

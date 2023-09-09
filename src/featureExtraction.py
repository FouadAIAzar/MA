import pandas as pd
from rdkit import Chem
from rdkit.Chem import Descriptors

# Read the CSV file
data = pd.read_csv('molecules.csv')

# Define a function to calculate descriptors for a given molecule
def calculate_descriptors(mol):
    descriptors = {}
    try:
        # Convert the SMILES string to an RDKit molecule object
        molecule = Chem.MolFromSmiles(mol)

        # Calculate descriptors
        for descriptor, calculator in Descriptors.descList:
            try:
                descriptors[descriptor] = calculator(molecule)
            except Exception as e:
                descriptors[descriptor] = None  # Set to None if calculation fails

    except Exception as e:
        print(f"Error processing molecule: {mol}")
        print(e)

    return descriptors

# Calculate descriptors for each molecule in the CSV file
all_descriptors = []
for index, row in data.iterrows():
    smile = row['Chromophore']
    emission = row['Emission max (nm)']
    if pd.notnull(emission):  # Check if the emission value is not NaN
        descriptors = calculate_descriptors(smile)
        descriptors['SMILES'] = smile  # Add SMILES to the descriptors dictionary
        all_descriptors.append(descriptors)
    print(str(index))

# Create a new DataFrame to store the descriptors
descriptors_df = pd.DataFrame(all_descriptors)

# Reorder columns to have SMILES first
cols = ['SMILES'] + [descriptor for descriptor, _ in Descriptors.descList]
descriptors_df = descriptors_df[cols]

# Save the result to a new CSV file
descriptors_df.to_csv('emission.csv', index=False)

# Print the total number of rows processed
print("Total number of rows processed:", len(all_descriptors))

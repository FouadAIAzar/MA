import os
from padelpy import from_smiles
import pandas as pd
from util import load_environment_variables

def padel(smiles_string):
    # Compute descriptors for the given SMILES string
    return from_smiles(smiles_string, threads = 4)

if __name__ == '__main__':
    # Load environment variables
    load_environment_variables()

    # Retrieve paths from environment variables
    DAT_PATH = os.getenv("DAT")
    RES_PATH = os.getenv("RES")

    # extract SMILES string from 'Chromophore' column from the CSV file at DAT_PATH
    data = pd.read_csv(f'{DAT_PATH}/2023-09-09/molecules.csv')
    smiles = data['Chromophore'].tolist()

    # Create empty list for descriptors
    descriptors = []

    for index, smile in enumerate(smiles):
        if index >= 1000:
            break
        try:
            descriptor = padel(smile)
            descriptor['Tag'] = index+1
            descriptor['SMILES'] = smile
            descriptors.append(descriptor)
            print(index)
        except Exception as e:
            print(f"Error processing SMILES string at index {index+1}: {smile}. Error: {e}")
            continue  # Skip to the next iteration
        
    # Convert list of dictionaries to a DataFrame
    df = pd.DataFrame(descriptors)

    # Move 'SMILES' column to the first position
    columns = ['Tag'] + [col for col in df if col != 'Tag']
    df = df[columns]
    
    # Export DataFrame to CSV
    df.to_csv(f'{RES_PATH}/descriptors.csv', index=False)

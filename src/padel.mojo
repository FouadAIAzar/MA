import os
from padelpy import from_smiles
import pandas as pd
from util import load_environment_variables

def padel(smiles_string):
    # Compute descriptors for the given SMILES string
    return from_smiles(smiles_string)
    


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
        descriptors.append(padel(smile))
        if ~(index % 10):
            print(index)

    # Convert list of dictionaries to a DataFrame
    df = pd.DataFrame(descriptors)

    # Export DataFrame to CSV
    df.to_csv(f'{RES_PATH}/descriptors.csv', index=True)


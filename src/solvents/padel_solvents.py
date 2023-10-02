import os
from padelpy import from_smiles
import pandas as pd
from util import load_environment_variables

def padel(smiles_string):
    # Compute descriptors for the given SMILES string
    return from_smiles(smiles_string)

def save_to_csv(descriptors, filepath, mode='w'):
    """Utility function to save descriptors to CSV."""
    df = pd.DataFrame(descriptors)
    df.to_csv(filepath, mode=mode, header=(mode == 'w'), index=False)

if __name__ == '__main__':
    # Load environment variables
    load_environment_variables()

    # Retrieve paths from environment variables
    DAT_PATH = os.getenv("DAT")
    RES_PATH = os.getenv("RES")

    # Extract SMILES string from 'Chromophore' column from the CSV file at DAT_PATH
    data = pd.read_csv(f'{DAT_PATH}/2023-10-02/solvents.csv')
    smiles = data['Solvent'].tolist()

    # Create empty lists for descriptors and errors
    descriptors = []
    error_descriptors = []

    for index, smile in enumerate(smiles):
        if index < 1:  # adjust this should you encounter another error
            continue
        try:
            descriptor = padel(smile)
            descriptor['Tag'] = index + 1
            descriptor['SMILES'] = smile
            descriptors.append(descriptor)
            print(f"Processed index: {index}")
        except Exception as e:
            print(f"Error processing SMILES string at index {index}: {smile}. Error: {e}")
            error_descriptors.append({"Tag": index + 1, "SMILES": smile, "Error": str(e)})
        
        # Save to file and clear cache every 50 processed entries
        if (index + 1) % 50 == 0:
            save_to_csv(descriptors, f'{RES_PATH}/2023-10-02/descriptors_solvent.csv', mode='a')
            descriptors.clear()
            print(f"Saved first {index+1} descriptors to file and cleared cache.")

    # Save any remaining descriptors and errors
    if descriptors:
        save_to_csv(descriptors, f'{RES_PATH}/2023-10-02/descriptors.csv', mode='a')
    if error_descriptors:
        pd.DataFrame(error_descriptors).to_csv(f'{RES_PATH}/2023-10-02/error_descriptors.csv', index=False)

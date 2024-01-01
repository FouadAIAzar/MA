from padelpy import from_smiles
import pandas as pd

def padel(smiles_string):
    # Compute descriptors for the given SMILES string
    return from_smiles(smiles_string, fingerprints = True,timeout=120)

def save_to_csv(descriptors, filepath, mode='w'):
    df = pd.DataFrame(descriptors)
    # Save to CSV
    df.to_csv(filepath, mode=mode, header=(mode == 'w'), index=False)

if __name__ == '__main__':
    # Extract SMILES string from 'Chromophore' column from the CSV file at DAT_PATH
    data = pd.read_csv(f'solvents.csv')
    smiles = data['Solvent'].tolist()

    # Start processing at index
    start_index = 0
    smiles = smiles[start_index:]

    # Create empty lists for descriptors and errors
    descriptors = []
    error_descriptors = []

    for index, smile in enumerate(smiles, start=start_index):
        try:
            descriptor = padel(smile)
            descriptor['Tag'] = index
            descriptor['SMILES'] = smile
            descriptors.append(descriptor)
            print(f"Processed index: {index}")
        except Exception as e:
            print(f"Error processing SMILES string at index {index}: {smile}. Error: {e}")
            error_descriptors.append({"Tag": index, "SMILES": smile, "Error": str(e)})
        
        # Save to file and clear cache every 50 processed entries
        if (index + 1) % 100 == 0:
            save_to_csv(descriptors, f'solvent_descriptors.csv', mode='a')
            descriptors.clear()
            print(f"Saved first {index+1} descriptors to file and cleared cache.")

    # Save any remaining descriptors and errors
    if descriptors:
        save_to_csv(descriptors, f'descriptors_solvents.csv', mode='a')
    if error_descriptors:
        pd.DataFrame(error_descriptors).to_csv(f'error_descriptors_solvents.csv', index=False)


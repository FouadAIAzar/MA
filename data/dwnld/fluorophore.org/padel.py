from padelpy import from_smiles
import pandas as pd

def padel(smiles_string):
    # Compute descriptors for the given SMILES string
    return from_smiles(smiles_string, fingerprints=True, timeout=60)

def save_to_csv(descriptors, filepath, mode='w'):
    # Convert the list of dictionaries to a DataFrame
    df = pd.DataFrame(descriptors)

    # Check if 'CAS Number', 'Name', and 'SMILES' are in the DataFrame and add them if not
    for col in ['CAS Number', 'Name', 'SMILES']:
        if col not in df.columns:
            df[col] = pd.NA

    # Arrange columns
    columns = ['CAS Number', 'Name', 'SMILES'] + [col for col in df.columns if col not in ['CAS Number', 'Name', 'SMILES']]
    df = df[columns]

    # Save to CSV
    df.to_csv(filepath, mode=mode, header=(mode == 'w'), index=False)


if __name__ == '__main__':
    # Extract SMILES string from the CSV file
    data = pd.read_csv('catalogue_with_valid_smiles.csv')
    cas_numbers = data['CAS Number'].tolist()
    names = data['Name'].tolist()
    smiles = data['SMILES'].tolist()

    # Create empty lists for descriptors and errors
    descriptors = []
    error_descriptors = []

    for index, (cas, name, smile) in enumerate(zip(cas_numbers, names, smiles)):
        try:
            descriptor = padel(smile)
            descriptor['CAS Number'] = cas
            descriptor['Name'] = name
            descriptor['SMILES'] = smile
            descriptors.append(descriptor)
            print(f"Processed index: {index}")
        except Exception as e:
            print(f"Error processing SMILES string at index {index} (CAS: {cas}): {smile}. Error: {e}")
            error_descriptors.append({"CAS Number": cas, "Name": name, "SMILES": smile, "Error": str(e)})
        
        # Save to file and clear cache every 50 processed entries (adjust as needed)
        if (index + 1) % 2 == 0:
            save_to_csv(descriptors, f'descriptors.csv', mode='a')
            descriptors.clear()
            print(f"Saved first {index+1} descriptors to file and cleared cache.")
        if error_descriptors:
            pd.DataFrame(error_descriptors).to_csv(f'error_descriptors.csv', index=False)
            error_descriptors.clear()

    # Save any remaining descriptors and errors
    if descriptors:
        save_to_csv(descriptors, f'descriptors.csv', mode='a')
    if error_descriptors:
        pd.DataFrame(error_descriptors).to_csv(f'error_descriptors.csv', index=False)

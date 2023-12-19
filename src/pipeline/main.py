import os
import pandas as pd
from util import load_environment_variables

def chunk_merge(input_file, reference_df, chunksize=10000, merge_column='Tag'):
    """
    Function to merge large CSV in chunks.
    """
    # Create an empty dataframe to store merged chunks
    merged_chunks = pd.DataFrame()

    # Process chunks
    for chunk in pd.read_csv(input_file, chunksize=chunksize):
        chunk[merge_column] = chunk[merge_column].astype(str)
        merged_chunk = pd.merge(chunk, reference_df, on=merge_column)
        merged_chunks = pd.concat([merged_chunks, merged_chunk], ignore_index=True)

    return merged_chunks

def main():
    load_environment_variables()
    DAT_PATH = os.getenv("DAT")
    RES_PATH = os.getenv("RES")

    # 1. Append Headers
    headers = pd.read_csv('header.csv', header=None).values.flatten().tolist()
    descriptors = pd.read_csv(f'{DAT_PATH}/main/descriptors.csv', header=None)
    descriptors.columns = headers
    descriptors.to_csv('descriptors_headers.csv', index=False)
    print("1. Headers Appended: Complete")

    # 2. Merge Input with Output (in chunks)
    molecules = pd.read_csv(f'{DAT_PATH}/main/molecules.csv')
    molecules['Tag'] = molecules['Tag'].astype(str)
    merged = chunk_merge('descriptors_headers.csv', molecules[['Tag', 'Emission max (nm)']])
    merged.to_csv('train_with_NaN.csv', index=False)
    print("2. Merger Complete")

    # 3. Remove NaNs
    df = pd.read_csv('train_with_NaN.csv')
    df = df.dropna()
    df.to_csv(f'{DAT_PATH}/main/train.csv', index=False)
    print("3. NaNs removed")

    # 4. Remove Temporary Files (optional)
    # os.remove('descriptors_headers.csv')
    # os.remove('train_with_NaN.csv')
    # print("4. Temporary files removed")

if __name__ == "__main__":
    main()


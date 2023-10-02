# Define Paths
import os
from util import load_environment_variables

load_environment_variables()
DAT_PATH = os.getenv("DAT")
RES_PATH = os.getenv("RES")

# Import necessary libraries
import csv
import pandas as pd
import numpy as np

def main():
    '''
    0. PaDEL Calculations
    
    This step is conducted outside of main for the simple fact that for a very large dataset, it will take days to compute.
    '''
    
    '''
    1. APPEND HEADERS
    ''' 
    # Open and read the headers csv file
    with open('headers.csv', 'r') as headers_file:         
        headers = list(csv.reader(headers_file))[0]

    # Open and read the descriptors backup csv file
    with open(f'{DAT_PATH}/2023-09-10/descriptors_backup.csv', 'r') as descriptors_file:
        descriptors = list(csv.reader(descriptors_file))

    # Combine headers and descriptors
    combined = [headers] + descriptors

    # Write the combined list back to the descriptors backup csv file
    with open('descriptors_headers.csv', 'w', newline='') as combined_file:
        writer = csv.writer(combined_file)
        writer.writerows(combined)

    print("1. Headers Appended: Complete")
    
    '''
    2. MERGE INPUT WITH OUTPUT
    '''
    # Read in CSV files
    descriptors_backup = pd.read_csv('descriptors_headers.csv')
    molecules = pd.read_csv(f'{DAT_PATH}/2023-09-09/molecules.csv')

    # Ensure that 'Tag' column is of type string for proper comparison
    descriptors_backup['Tag'] = descriptors_backup['Tag'].astype(str)
    molecules['Tag'] = molecules['Tag'].astype(str)

    # Perform an inner merge on 'Tag' to get matching rows
    merged = pd.merge(descriptors_backup, molecules[['Tag', 'Absorption max (nm)']], on='Tag')

    # Write the new dataframe to train.csv
    merged.to_csv('train_with_NaN.csv', index=False)

    print("2. Merger Complete")

    '''
    3. REMOVE NANS
    '''
    # read the csv file
    df = pd.read_csv('train_with_NaN.csv')

    # remove the rows with NaN values
    df = df.dropna()

    # write back to csv
    df.to_csv(f'{DAT_PATH}/2023-09-10/train_absorption.csv', index=False)

    print("3. Nans removed")

    '''
    4. REMOVE TEMPORARY FILES
    '''
    
    # os.remove(filename)
    
    # print("4. remove temporary files")

if __name__ == "__main__":
    main()

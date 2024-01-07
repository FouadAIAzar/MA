import os
import pandas as pd

# Directory containing the subfolders
dyes_directory = 'dyes'

# Iterate through each subfolder in the dyes directory
for folder in os.listdir(dyes_directory):
    subfolder_path = os.path.join(dyes_directory, folder)
    spectra_file_path = os.path.join(subfolder_path, 'spectra.csv')

    # Check if spectra.csv exists in the folder
    if os.path.exists(spectra_file_path):
        # Read the CSV file
        df = pd.read_csv(spectra_file_path, delimiter=';')

        # Check and extract Absorption data
        if 'Absorption wavelength (nm)' in df and 'normalized Absorption' in df:
            ab_df = df[['Absorption wavelength (nm)', 'normalized Absorption']].copy()
            ab_df.columns = ['WL', 'AB']
            ab_df.to_csv(os.path.join(subfolder_path, 'AB.csv'), index=False)

        # Check and extract Emission data
        if 'emission wavelength (nm)' in df and 'Normalized emission' in df:
            em_df = df[['emission wavelength (nm)', 'Normalized emission']].copy()
            em_df.columns = ['WL', 'EM']
            em_df.to_csv(os.path.join(subfolder_path, 'EM.csv'), index=False)

        # Check and extract Excitation data
        if 'Exitation wavelength (nm)' in df and 'normalized Exitation' in df:
            ex_df = df[['Exitation wavelength (nm)', 'normalized Exitation']].copy()
            ex_df.columns = ['WL', 'EX']
            ex_df.to_csv(os.path.join(subfolder_path, 'EX.csv'), index=False)

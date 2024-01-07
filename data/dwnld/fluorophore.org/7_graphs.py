import os
import pandas as pd
import matplotlib.pyplot as plt

def plot_spectra(df, cas_number, folder_path):
    try:
        plt.figure(figsize=(10, 6))

        # Plot Absorption if the column exists
        if 'Absorption wavelength (nm)' in df and 'normalized Absorption' in df:
            plt.plot(df['Absorption wavelength (nm)'], df['normalized Absorption'], color='blue', label='Normalized Absorption')

        # Plot Emission if the column exists
        if 'emission wavelength (nm)' in df and 'Normalized emission' in df:
            plt.plot(df['emission wavelength (nm)'], df['Normalized emission'], color='red', label='Normalized Emission')

        # Plot Excitation if the column exists
        if 'Exitation wavelength (nm)' in df and 'normalized Exitation' in df:
            plt.plot(df['Exitation wavelength (nm)'], df['normalized Exitation'], color='green', label='Normalized Excitation')

        plt.xlabel('Wavelength (nm)')
        plt.ylabel('Intensity (AU)')
        plt.title(f'Spectra for CAS {cas_number}')
        plt.legend()
        plt.grid(True)
        plt.savefig(os.path.join(folder_path, f'{cas_number}_spectra.png'))
        plt.close()
        print(f'Plot saved for CAS {cas_number}')
    except Exception as e:
        print(f'Error occurred while plotting CAS {cas_number}: {e}')

# Directory containing the subfolders
dyes_directory = 'dyes'

# Iterate through each subfolder in the dyes directory
for cas_number in os.listdir(dyes_directory):
    subfolder_path = os.path.join(dyes_directory, cas_number)
    if os.path.isdir(subfolder_path):  # Check if it's a directory
        for file in os.listdir(subfolder_path):
            file_path = os.path.join(subfolder_path, file)
            # Check if the file is a CSV
            if file_path.lower().endswith('.csv'):
                try:
                    df = pd.read_csv(file_path, delimiter=';', encoding='ISO-8859-1')
                    plot_spectra(df, cas_number, subfolder_path)
                except UnicodeDecodeError as e:
                    print(f'Unicode decode error for file {file_path}: {e}')
                except Exception as e:
                    print(f'Error occurred while processing file {file_path}: {e}')
            else:
                print(f'Skipped non-CSV file: {file_path}')

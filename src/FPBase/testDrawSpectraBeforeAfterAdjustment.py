import pandas as pd
import os
import matplotlib.pyplot as plt
import random

# Setting directory paths
current_directory = os.getcwd()
input_folder = os.path.join(current_directory, 'spectra')
output_folder = os.path.join(current_directory, 'adjusted_spectra')

# Get a list of all csv files in the input_folder
csv_files = [f for f in os.listdir(input_folder) if f.endswith('.csv')]
if not csv_files:
    print("No CSV files found in the 'spectra' directory.")
    exit()

# Randomly select a file from the list
selected_file = random.choice(csv_files)

# Load the original and adjusted data
original_data_path = os.path.join(input_folder, selected_file)
adjusted_data_path = os.path.join(output_folder, selected_file)

original_df = pd.read_csv(original_data_path)
adjusted_df = pd.read_csv(adjusted_data_path)

# Plot the data
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(original_df['Wavelength'], original_df['Intensity'], label='Original Spectrum')
plt.title(f"Original Spectrum - {selected_file}")
plt.xlabel('Wavelength')
plt.ylabel('Intensity')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(adjusted_df['Wavelength'], adjusted_df['Intensity'], label='Adjusted Spectrum', color='red')
plt.title(f"Adjusted Spectrum - {selected_file}")
plt.xlabel('Wavelength')
plt.ylabel('Intensity')
plt.legend()

plt.tight_layout()
plt.show()


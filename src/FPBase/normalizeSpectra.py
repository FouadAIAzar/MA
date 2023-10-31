import os
import pandas as pd

# Define the directory paths
current_directory = os.getcwd()
input_folder = os.path.join(current_directory, 'spectra')
output_folder = os.path.join(current_directory, 'adjusted_spectra')

# Create the output directory if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Get a list of all CSV files in the input_folder
csv_files = [f for f in os.listdir(input_folder) if f.endswith('.csv')]

# Set the fixed wavelengths
fixed_min_wavelength = 190
fixed_max_wavelength = 900

# Identify the smallest difference between wavelengths
smallest_difference = float('inf')
for file in csv_files:
    df = pd.read_csv(os.path.join(input_folder, file))
    local_difference = df['Wavelength'].diff().min()
    smallest_difference = min(smallest_difference, local_difference)

# Generate the new universal wavelength range
new_wavelengths = list(range(fixed_min_wavelength, fixed_max_wavelength + 1, int(smallest_difference)))

# Process each CSV file
for file in csv_files:
    print(f"Processing {file}...")
    filepath = os.path.join(input_folder, file)
    df = pd.read_csv(filepath)
    
    # Create a DataFrame with the new wavelength range
    full_range_df = pd.DataFrame({'Wavelength': new_wavelengths})
    
    # Merge with the original data
    merged_df = pd.merge(full_range_df, df, on='Wavelength', how='left')
    
    # Fill NaNs in the 'Intensity' column with zeros
    merged_df['Intensity'].fillna(0, inplace=True)
    
    # Save the adjusted data to the new folder
    output_filepath = os.path.join(output_folder, file)
    merged_df.to_csv(output_filepath, index=False)

print("Processing complete!")

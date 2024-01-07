import os
import pandas as pd

# Directory containing the CSV files
csv_directory = '.'

# Directory to store the substance folders
substances_directory = './substances'

# Check if the substances directory exists, if not create it
if not os.path.exists(substances_directory):
    os.makedirs(substances_directory)

# Initialize a set to store unique substance names
unique_substances = set()

# Process each CSV file in the directory
for filename in os.listdir(csv_directory):
    if filename.endswith('.csv'):
        try:
            csv_path = os.path.join(csv_directory, filename)

            # Read the CSV file
            df = pd.read_csv(csv_path)

            # Extract the Wavelength column
            wavelengths = df['Wavelength']

            # Process each substance in the CSV
            for column in df.columns:
                if column != 'Wavelength':
                    substance, spectra_type = column.rsplit(' ', 1)
                    unique_substances.add(substance)

                    # Create a directory for the substance if it doesn't exist
                    substance_dir = os.path.join(substances_directory, substance)
                    if not os.path.exists(substance_dir):
                        os.makedirs(substance_dir)

                    # Save the data for this spectra type
                    spectra_data = pd.concat([wavelengths, df[column]], axis=1)
                    spectra_file = os.path.join(substance_dir, f'{spectra_type}.csv')
                    spectra_data.to_csv(spectra_file, index=False)
        except Exception as e:
            print(f"Error processing {filename}: {e}. Skipping to next file.")

# Save the unique substances to a file
with open('catalogue.txt', 'w') as file:
    for substance in sorted(unique_substances):
        file.write(substance + '\n')

print("Processing complete.")

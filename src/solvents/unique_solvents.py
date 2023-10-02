import pandas as pd

# Read the molecules.csv file
df = pd.read_csv('~/MA/data/2023-09-09/molecules.csv')

# Extract the unique entries from the 'solvent' column
unique_solvent = df['Solvent'].drop_duplicates()

# Make sure the output directory exists 
import os
output_dir = '~/MA/results/2023-10-02'
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, 'solvents.csv')

# Write these unique entries to a new CSV file
unique_solvent.to_csv(output_path, index=False)

print(f'Unique solvents have been written to: {output_path}')


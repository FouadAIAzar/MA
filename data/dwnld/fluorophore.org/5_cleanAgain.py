import pandas as pd

# Read the CSV file
df = pd.read_csv('catalogue_with_smiles.csv')

# Normalize empty values and convert them to NaN
df['SMILES'] = df['SMILES'].replace(['', ' ', None], pd.NA)

# Filter out rows with NaN SMILES entries
filtered_df = df.dropna(subset=['SMILES'])

# Save the filtered data to a new CSV file
filtered_df.to_csv('catalogue_with_valid_smiles.csv', index=False)

print("Rows with empty SMILES entries removed. New CSV file saved as 'catalogue_with_valid_smiles.csv'.")

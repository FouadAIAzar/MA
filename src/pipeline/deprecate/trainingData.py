import pandas as pd

# Read in CSV files
descriptors_backup = pd.read_csv('descriptors_backup.csv')
molecules = pd.read_csv('molecules.csv')

# Ensure that 'Tag' column is of type string for proper comparison
descriptors_backup['Tag'] = descriptors_backup['Tag'].astype(str)
molecules['Tag'] = molecules['Tag'].astype(str)

# Perform an inner merge on 'Tag' to get matching rows
merged = pd.merge(descriptors_backup, molecules[['Tag', 'Emission max (nm)']], on='Tag')

# Write the new dataframe to train.csv
merged.to_csv('train.csv', index=False)


import pandas as pd

# Load the CSV data
data = pd.read_csv('combined_descriptors.csv')

# Using iloc to refer to the 1876th column (index 1875)
data = data[data.iloc[:, 1876] != "COC(=O)/C=C/c1ccc2ccc3cccc4ccc1c2c34"]

# Save the cleaned data back to the CSV file
data.to_csv('combined_descriptors.csv', index=False)


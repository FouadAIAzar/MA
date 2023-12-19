import pandas as pd

# Reading the CSV file
data = pd.read_csv('descriptors.csv', header=None)

# Filtering rows based on the condition
filtered_data = data[(data[0] >= 12858) & (data[0] <= 19397)]

# Saving the filtered data to a new CSV
filtered_data.to_csv('filtered_descriptors.csv', header=False, index=False)


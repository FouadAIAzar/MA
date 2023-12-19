import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def calculate_bins(data):
    """
    Calculate the number of bins using the Freedman-Diaconis rule, accounting for NaN values.
    """
    data = data.dropna()  # Remove NaN values from the data
    q75, q25 = np.percentile(data, [75, 25])
    iqr = q75 - q25
    bin_width = (2 * iqr) / (len(data) ** (1/3))
    num_bins = int((max(data) - min(data)) / bin_width)
    return num_bins

# Read the CSV file
df = pd.read_csv('molecules.csv')

# Extract the "emission max [nm]" column
emission_max = df['Molecular weight (g mol-1)']

# Calculate the number of bins
num_bins = calculate_bins(emission_max)

# Plot the histogram
plt.hist(emission_max, bins=num_bins, edgecolor='black')

title = 'Histogram of Molecular Weight'
# Customize the plot
plt.xlabel('Molecular weight [g/mol]')
plt.ylabel('Frequency')
plt.title(title)
plt.grid(True)


plt.savefig(title)

# Display the plot
plt.show()

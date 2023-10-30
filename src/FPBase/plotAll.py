import os
import pandas as pd
import matplotlib.pyplot as plt

# Define the directory paths
current_directory = os.getcwd()
output_folder = os.path.join(current_directory, 'adjusted_spectra')

# Get a list of all CSV files in the output_folder
csv_files = [f for f in os.listdir(output_folder) if f.endswith('.csv')]

# Set up the figure for plotting
plt.figure(figsize=(14, 8))

# Plot each adjusted spectrum
for file in csv_files:
    filepath = os.path.join(output_folder, file)
    df = pd.read_csv(filepath)
    plt.plot(df['Wavelength'], df['Intensity'], label=file)

# Customize the plot
plt.title('Adjusted Spectra')
plt.xlabel('Wavelength')
plt.ylabel('Intensity')
plt.legend(loc='upper right', fontsize='small')
plt.grid(True)

# Show the plot
plt.tight_layout()
plt.show()


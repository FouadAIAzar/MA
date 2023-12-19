import pandas as pd
from sklearn.model_selection import train_test_split

# Load the CSV file
file_path = 'complete_set.csv'  # Replace with your CSV file path
data = pd.read_csv(file_path)

# Separate 'Emission max (nm)' column
emission_max = data['Emission max (nm)']

# Select the first 1875 columns excluding 'Emission max (nm)'
data_selected = data.iloc[:, :1875]

# Split the dataset into training (80%) and testing (20%) sets
X_train, X_test, y_train, y_test = train_test_split(data_selected, emission_max, test_size=0.2, random_state=42)

# Reattach 'Emission max (nm)' to the training and testing sets
train = pd.concat([X_train, y_train.reset_index(drop=True)], axis=1)
test = pd.concat([X_test, y_test.reset_index(drop=True)], axis=1)

# Save the datasets to CSV files
train.to_csv('train.csv', index=False)
test.to_csv('test.csv', index=False)

print("Data has been split and saved as 'train.csv' and 'test.csv'")


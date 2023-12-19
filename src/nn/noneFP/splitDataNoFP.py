import pandas as pd

# Read the complete_set.csv file
df = pd.read_csv('complete_set.csv')

# Move the 'Emission max (nm)' column to the 3rd column
df.insert(2, 'Emission max (nm)', df.pop('Emission max (nm)'))

# Take the first 1877 columns and discard the rest
df = df.iloc[:, :1877]

# Split the remaining rows in a ratio of 20-80
train_df = df.sample(frac=0.8, random_state=42)
test_df = df.drop(train_df.index)

# Save the train and test dataframes as CSV files
train_df.to_csv('train.csv', index=False)
test_df.to_csv('test.csv', index=False)

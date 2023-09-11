import pandas as pd

# Read both csv files into pandas dataframes
descriptors = pd.read_csv("descriptors.csv", header=None)
molecules = pd.read_csv("molecules.csv")

# Rename the first column of descriptors dataframe for easier merging
descriptors = descriptors.rename(columns={0: "Tag"})

# Merge the dataframes on the 'Tag' column
merged_data = pd.merge(descriptors, molecules[["Tag", "Emission max (nm)"]], on="Tag", how="left")

# Append 'Emission max [nm]' to descriptors and drop the first two columns (i.e., 'Tag' and 'Emission max [nm]')
train_data = pd.concat([merged_data["Emission max (nm)"], merged_data.iloc[:, 2:]], axis=1)

# Write to train.csv
train_data.to_csv("train.csv", index=False)


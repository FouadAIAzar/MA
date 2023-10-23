import pandas as pd
print(f"The number of NaN values in the 'Emission max (nm)' column is: {pd.read_csv('train_with_NaN.csv')['Emission max (nm)'].isna().sum()}")


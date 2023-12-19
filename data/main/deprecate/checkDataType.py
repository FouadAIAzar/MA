import pandas as pd

# Load your data
df = pd.read_csv('descriptors3.csv')

# Check the datatype of the 1876th column
# Python is zero-indexed, so the 1876th column is indexed as 1875
column_index = 1875
print(df.iloc[:, column_index].dtype)

# Check for columns in the DataFrame with different datatypes
for column in df.columns:
    if df[column].dtype != df.iloc[:, column_index].dtype:
        print(f'The column {column} is of a different datatype ({df[column].dtype})')


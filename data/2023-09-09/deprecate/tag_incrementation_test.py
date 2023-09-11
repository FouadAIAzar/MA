import pandas as pd

df = pd.read_csv('molecules.csv')

prev_value = df['Tag'][0] - 1  # Initial value is set to minus one for the first comparison
for i, value in enumerate(df['Tag']):
    if value != prev_value + 1:
        print(f"The value at index {i} is not incremented by one from the previous value.")
    prev_value = value

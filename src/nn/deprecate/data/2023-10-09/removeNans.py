# necessary imports
import pandas as pd
import numpy as np

# read the csv file
df = pd.read_csv('train.csv')

# remove the rows with NaN values
df = df.dropna()

# write back to csv
df.to_csv('train_nonnan.csv', index=False)


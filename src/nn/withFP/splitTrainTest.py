import pandas as pd
from sklearn.model_selection import train_test_split

def split_csv_file(file_path, train_size=0.8, random_state=42):
    # Read the CSV file
    data = pd.read_csv(file_path)

    train_data, test_data = train_test_split(data, train_size=train_size, test_size=1-train_size, random_state=random_state)

    train_data.to_csv('train.csv', index=False)
    test_data.to_csv('test.csv', index=False)

    print("Data has been split and saved as 'train_data.csv' and 'test_data.csv'.")

file_path = 'complete_set.csv'
split_csv_file(file_path)


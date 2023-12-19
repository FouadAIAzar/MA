import pandas as pd

def remove_extra_columns(filename):
    # Read the data from CSV file
    data = pd.read_csv(filename)

    # Check if the data has more than 1876 columns
    if data.shape[1] > 1877:
        # Select columns up to the 1876th
        data = data.iloc[:, :1877]
    
    # Save the updated DataFrame back to CSV
    data.to_csv('updated_file.csv', index=False)
    print(f"New file saved as 'updated_file.csv' with {data.shape[1]} columns.")

remove_extra_columns('descriptors.csv')


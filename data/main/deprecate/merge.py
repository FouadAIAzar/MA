import pandas as pd

# Define chunk size for reading large files
chunk_size = 10000  # Adjust this based on your system's memory

# Define file paths
file1 = 'descriptors2.csv'
file2 = 'filtered_descriptors.csv'
output_file = 'combined_descriptors.csv'

# Read the first file entirely
df1 = pd.read_csv(file1, header=None, chunksize=chunk_size)
df_combined = pd.concat(df1, ignore_index=True)

# Function to filter rows based on ID condition
def filter_rows(df_chunk):
    return df_chunk[df_chunk.iloc[:, 0] > 12858]

# Read the second file in chunks and filter
df2 = pd.read_csv(file2, header=None, chunksize=chunk_size)
filtered_chunks = [filter_rows(chunk) for chunk in df2]

# Combine filtered data from the second file
df_filtered = pd.concat(filtered_chunks, ignore_index=True)

# Combine both dataframes
final_df = pd.concat([df_combined, df_filtered], ignore_index=True)

# Save the combined dataframe to a new CSV file
final_df.to_csv(output_file, index=False, header=False)


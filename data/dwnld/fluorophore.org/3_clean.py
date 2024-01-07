import pandas as pd
import re

# Function to check if CAS number is valid (only contains digits and hyphens)
def is_valid_cas(cas_number):
    if pd.isna(cas_number) or not isinstance(cas_number, str):
        return False
    return bool(re.fullmatch(r"[0-9\-]+", cas_number))

# Read the CSV file
df = pd.read_csv('catalogue.csv')

# Filter out rows with invalid CAS numbers
valid_cas_df = df[df['CAS Number'].apply(is_valid_cas)]

# Save the filtered data to a new CSV file
valid_cas_df.to_csv('filtered_catalogue.csv', index=False)

print("Filtered data saved to 'filtered_catalogue.csv'.")

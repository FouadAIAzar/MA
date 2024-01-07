import os
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to create a directory if it doesn't exist
def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

# Function to download and save the CSV file
def download_csv(url, cas_number, base_url="https://www.fluorophores.tugraz.at"):
    try:
        response = requests.get(url, verify=False)  # Bypass SSL verification
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            download_link = soup.find('a', title='download spectra as csv')['href']
            # Check if the download link is a relative URL
            if not download_link.startswith('http'):
                download_link = base_url + download_link
            csv_response = requests.get(download_link, verify=False)  # Bypass SSL verification
            if csv_response.status_code == 200:
                file_path = os.path.join('dyes', cas_number, 'spectra.csv')
                with open(file_path, 'wb') as file:
                    file.write(csv_response.content)
                print(f"CSV for CAS {cas_number} downloaded successfully.")
            else:
                print(f"Failed to download CSV for CAS {cas_number}")
        else:
            print(f"Failed to access page for CAS {cas_number}")
    except Exception as e:
        print(f"Error occurred for CAS {cas_number}: {e}")


# Read the CSV file
df = pd.read_csv('catalogue_with_valid_smiles.csv')

# Create a 'dyes' directory
create_directory('dyes')

# Process each row in the DataFrame
for index, row in df.iterrows():
    cas_number = row['CAS Number']
    url = row['URL'] + '#cont_spectra'

    # Create a subdirectory for each CAS number
    cas_directory = os.path.join('dyes', cas_number)
    create_directory(cas_directory)

    # Download and save the CSV file
    download_csv(url, cas_number)

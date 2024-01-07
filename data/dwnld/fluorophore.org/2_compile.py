import requests
from bs4 import BeautifulSoup
import pandas as pd
import requests.packages.urllib3

# Suppress the InsecureRequestWarning
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

# Function to extract h1, CAS number, and URL from a given URL
def extract_data(url):
    try:
        response = requests.get(url, verify=False)  # Bypass SSL verification
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            h1 = soup.find('h1').text.strip()
            cas_number = soup.find('label', text='CAS number:').find_next('span').text.strip()
            return h1, cas_number, url
        else:
            print(f"Failed to access {url}")
            return None, None, None
    except Exception as e:
        print(f"Error occurred for {url}: {e}")
        return None, None, None

# Read the TSV file
file_path = 'table.tsv'  # Replace with your file path
data = pd.read_csv(file_path, sep='\t', header=None)

# Extract data and save to a new list
extracted_data = []
for url in data[0]:
    h1, cas, url = extract_data(url)
    if h1 and cas:
        extracted_data.append([h1, cas, url])

# Convert the list to a DataFrame and save to CSV
df = pd.DataFrame(extracted_data, columns=['Name', 'CAS Number', 'URL'])
df.to_csv('catalogue.csv', index=False)

print("Data extraction complete. CSV file saved as 'catalogue.csv'.")

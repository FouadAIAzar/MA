# Re-importing necessary libraries and redefining file paths since the code execution state was reset
from bs4 import BeautifulSoup
import csv

# File path for the original HTML file and the updated TSV file
file_path = '/mnt/data/table.html'
updated_tsv_file_path = '/mnt/data/updated_converted_table.tsv'

# Reading the HTML file
with open(file_path, 'r') as file:
    html_content = file.read()

# Parsing the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find('tbody')
rows = table.find_all('tr')

# Preparing to write to TSV with updated format
tsv_content = []
base_url = "https://www.fluorophores.tugraz.at"

for row in rows:
    cols = row.find_all('td')
    row_data = []
    for col in cols:
        # Extracting href if available and concatenating with base URL
        href = col.find('a', href=True)
        if href:
            row_data.append(base_url + href['href'])
        else:
            row_data.append(col.text.strip())
    tsv_content.append(row_data)

# Writing to the updated TSV file
with open(updated_tsv_file_path, 'wt', newline='', encoding='utf-8') as out_file:
    tsv_writer = csv.writer(out_file, delimiter='\t')
    for row in tsv_content:
        tsv_writer.writerow(row)

updated_tsv_file_path


from bs4 import BeautifulSoup

def html_table_to_csv(html_content, csv_filename):
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")
    
    # Find the first table in the HTML content
    table = soup.find("table")
    
    # If no table is found, print a message and return
    if not table:
        print("No table found in the provided HTML content!")
        return

    # Open the desired CSV file for writing
    with open(csv_filename, "w") as csv_file:
        # Loop through each row in the table
        for row in table.find_all("tr"):
            cells = row.find_all(["td", "th"])  # consider both table data and header cells
            # Extract text from each cell and wrap it with double quotes to handle commas
            csv_row = [f'"{cell.get_text().strip()}"' for cell in cells]
            # Join the cells with commas and write to the CSV file
            csv_file.write(",".join(csv_row) + "\n")

if __name__ == "__main__":
    # You can read the HTML content from a file or any other source
    with open("buyel2023_table.html", "r") as f:
        html_content = f.read()

    # Convert the table from the HTML content to a CSV file
    html_table_to_csv(html_content, "output.csv")
    print("CSV file has been created as output.csv!")


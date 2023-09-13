import csv
import psycopg2
from config import DB_CONFIG

# Connect to PostgreSQL
conn = psycopg2.connect(**DB_CONFIG)
cur = conn.cursor()

# Read the CSV file for headers
with open("headersSanitized.csv", "r") as f:
    reader = csv.reader(f)
    headers = next(reader)  # Get the first row

# First and second headers as placeholders
first_header = headers[0]
second_header = headers[1]

# Third and onward headers
other_headers = ", ".join([f"{header} float" for header in headers[2:1600]])

# Create the table
cur.execute(f"""
    DROP TABLE IF EXISTS descriptors;
    CREATE TABLE descriptors (
        {first_header} serial PRIMARY KEY,
        {second_header} TEXT,
        {other_headers}
    );
""")
conn.commit()
cur.close()
conn.close()


# # Open and read the CSV file
# with open('descriptors_backup.csv', 'r') as f:
#     reader = csv.reader(f)
#     header = next(reader)

#     # Prepare insert statement
#     insert_query = f"INSERT INTO descriptors ({','.join(header)}) VALUES ({','.join(['%s' for _ in header])})"

#     # Insert rows
#     for row in reader:
#         cur.execute(insert_query, row[0:1600])

# # Commit changes and close
# conn.commit()
import csv
import psycopg2
from config import DB_CONFIG

# Connect to PostgreSQL
conn = psycopg2.connect(**DB_CONFIG)
cur = conn.cursor()

# Create table
cur.execute("""
    DROP TABLE IF EXISTS descriptors;
    CREATE TABLE your_table_name (
        id serial PRIMARY KEY,
        Name TEXT,
        {columns}
    );
""".format(columns=", ".join([f"column{i+3} float" for i in range(1598)])))

# Open and read the CSV file
with open('descriptors_backup.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)

    # Skip the first column
    header = header[1:]

    # Prepare insert statement
    insert_query = f"INSERT INTO your_table_name ({','.join(header)}) VALUES ({','.join(['%s' for _ in header])})"

    # Insert rows
    for row in reader:
        cur.execute(insert_query, row[1:])

# Commit changes and close
conn.commit()
cur.close()
conn.close()


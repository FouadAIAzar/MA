import csv
import psycopg2
from config import DB_CONFIG

conn = psycopg2.connect(**DB_CONFIG)
cur = conn.cursor()

with open('molecules.csv', 'r') as file:
    reader = csv.reader(file)
    
    # Skip header row
    next(reader)

    for row in reader:
        # Replace 'NaN' values with None
        row = [None if str(value) == 'NaN' else value for value in row]
        
        placeholders = ', '.join(['%s'] * len(row))
        sql = f"INSERT INTO fluorophores VALUES ({placeholders})"
        cur.execute(sql, row)

conn.commit()
cur.close()
conn.close()


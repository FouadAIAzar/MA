import psycopg2

conn = psycopg2.connect(database="", user='postgres', password='EbeneezerAzar271828', host='', port='5432')
conn.autocommit = True
cursor = conn.cursor()

# Uncomment the following block if you want to create the table (make sure to adjust the data types accordingly).
# sql = '''CREATE TABLE molecules (
#     Tag INTEGER,
#     Chromophore VARCHAR(100),
#     Solvent VARCHAR(100),
#     "Absorption max (nm)" NUMERIC,
#     "Emission max (nm)" NUMERIC,
#     "Lifetime (ns)" NUMERIC,
#     "Quantum yield" NUMERIC,
#     "log(e/mol-1 dm3 cm-1)" NUMERIC,
#     "abs FWHM (cm-1)" NUMERIC,
#     "emi FWHM (cm-1)" NUMERIC,
#     "abs FWHM (nm)" NUMERIC,
#     "emi FWHM (nm)" NUMERIC,
#     "Molecular weight (g mol-1)" NUMERIC,
#     Reference VARCHAR(255)
# );'''

# cursor.execute(sql)

failed_rows = []
cur = conn.cursor()
with open('C:\\Users\\user\\Desktop\\Flurine2\\scripts\\molecules.csv', 'r') as f:
    next(f)  # Skip the header row.
    for line in f:
        try:
            cur.copy_from(f, 'molecules', sep=',')
        except psycopg2.Error as e:
            # Handle the error for the current row.
            print(f"Failed to copy a row: {e}")
            # Store the TAG from the failed row (assuming TAG is the first column).
            tag = line.strip().split(',')[0]
            failed_rows.append(tag)

conn.commit()

# Print all the failed TAGs.
print("Failed rows' TAGs:")
print(failed_rows)

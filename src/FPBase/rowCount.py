with open('proteins_info.csv', 'r') as f:
    row_count = sum(1 for _ in f)

# Subtracting 1 for the header row
if row_count > 0:
    row_count -= 1

print(f"Number of rows in the file: {row_count}")


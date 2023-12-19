import csv

def sanitize_header(header):
    sanitized = "".join(char if char.isalnum() else "_" for char in header)
    if sanitized[0].isdigit():
        sanitized = "_" + sanitized
    return sanitized

# Replace 'input.csv' with your input file name
input_filename = 'headers.csv'
# Replace 'output.csv' with your desired output file name
output_filename = 'headersSanitized.csv'

with open(input_filename, 'r') as infile, open(output_filename, 'w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    
    headers = next(reader)
    sanitized_headers = [sanitize_header(header) for header in headers]
    writer.writerow(sanitized_headers)
    
    for row in reader:
        writer.writerow(row)


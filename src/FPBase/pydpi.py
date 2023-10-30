import csv
from pydpi.pypro import AAComposition, CTD

# Step 1: Read the CSV file named protein_info.csv
with open("protein_info.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    
    # Step 2: Extract the seq column
    for row in reader:
        seq = row['seq']
        
        # Step 3: Calculate amino acid composition
        aac = AAComposition.CalculateAAComposition(seq)
        
        # Step 4: Calculate CTD
        ctd = CTD.CalculateCTD(seq)
        
        # Step 5: Print the results
        print(f"Sequence: {seq}")
        print("Amino Acid Composition:", aac)
        print("CTD:", ctd)
        print("-" * 40)  # Separator for better readability


import json
import csv
import os

# Load the original JSON data
with open("filtered_proteins.json", "r") as file:
    data = json.load(file)

# Ensure the 'spectra' directory exists
if not os.path.exists('spectra'):
    os.makedirs('spectra')

# Create a general CSV for all proteins
with open("proteins_info.csv", "w", newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=["id", "seq", "pdb", "name", "state_name", "state_slug", "emMax", "exMax", "spectra_filepath"])
    writer.writeheader()

    for protein in data['data']['proteins']:
        for state in protein['states']:
            for spectrum in state['spectra']:
                # Check if the spectrum is of type "EM"
                if spectrum['subtype'] == "EM":
                    # Write general protein and state info to main CSV
                    row = {
                        "id": protein["id"],
                        "seq": protein["seq"],
                        "pdb": protein["pdb"],
                        "name": protein["name"],
                        "state_name": state["name"],
                        "state_slug": state["slug"],
                        "emMax": state["emMax"],
                        "exMax": state["exMax"],
                        "spectra_filepath": f"~/spectra/{protein['id']}_em.csv"
                    }
                    writer.writerow(row)

                    # Write spectrum data to separate CSV
                    with open(f"spectra/{protein['id']}_em.csv", "w", newline='') as spec_csv:
                        spec_writer = csv.writer(spec_csv)
                        spec_writer.writerow(["Wavelength", "Intensity"])
                        for point in spectrum['data']:
                            spec_writer.writerow([point[0], point[1]])  # Adjusted this line


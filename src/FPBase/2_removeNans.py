import json

# Assuming your json data is stored in 'input.json'
with open('proteins.json', 'r') as f:
    data = json.load(f)

initial_count = len(data['data']['proteins'])
filtered_proteins = []

for protein in data['data']['proteins']:
    # Check for non-empty seq
    if not protein['seq']:
        continue

    filtered_states = []

    for state in protein['states']:
        # Check for non-empty spectra
        if not state['spectra']:
            continue

        # Only keep spectra with subtype "EM"
        state['spectra'] = [s for s in state['spectra'] if s['subtype'] == 'EM']

        if state['spectra']:
            filtered_states.append(state)

    if filtered_states:
        protein['states'] = filtered_states
        filtered_proteins.append(protein)

data['data']['proteins'] = filtered_proteins
final_count = len(filtered_proteins)

# Save the filtered data to 'output.json'
with open('filtered_proteins.json', 'w') as f:
    json.dump(data, f, indent=4)

print(f"Total Entries: {initial_count}")
print(f"Entries Filtered Out: {initial_count - final_count}")
print(f"Entries Remaining: {final_count}")


## FPbase Protein Data Fetcher

This script fetches protein data from the FPbase GraphQL endpoint and saves the fetched data as a JSON file.

### Quick Start

1. Ensure you have the required Python libraries installed:
```bash
pip install requests
```

2. Run the script:
```bash
python your_script_name.py
```
Replace `your_script_name.py` with the actual filename if it's different.

### How it works

1. A GraphQL query is defined to fetch:
   - Protein details like ID, sequence, pdb, and name.
   - Details about the states of these proteins, including the name, slug, emission max, excitation max, and spectra subtype and data.

2. A POST request is sent to the FPbase GraphQL endpoint with the query.

3. Upon receiving a successful response (HTTP 200), the data is saved to a JSON file named `proteins.json`.

4. If the request is not successful, the script prints out the status code and the response text.

### Dependencies

- `requests`: For sending HTTP requests.
- `json`: For parsing and saving JSON data.

### Note

Ensure you have proper permissions and you adhere to the terms of service/use of FPbase when fetching data. The rate of requests and the amount of data fetched might be subject to limits as set by FPbase.

---

### License

Unless specified otherwise, this script is provided "as is" without any warranty. Use at your own risk. Consider mentioning the source or providing attribution if you use or adapt the script in your work.


import requests
import json

# FPbase GraphQL endpoint
GRAPHQL_URL = "https://www.fpbase.org/graphql/"

# Your GraphQL query
graphql_query = """
{
  proteins {
    id
    seq
    pdb
    name
    states {
      name
      slug
      emMax
      exMax
      spectra {
        subtype
        data
      }
    }
  }
}
"""

# Set up headers just for JSON
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

# Send the request
response = requests.post(GRAPHQL_URL, data=json.dumps({"query": graphql_query}), headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Load data from the response
    data = response.json()

    # Save the data to a file named proteins.json
    with open('proteins.json', 'w') as file:
        json.dump(data, file, indent=4)

    print("Data saved to proteins.json!")
else:
    print("Failed to fetch data. Status code:", response.status_code)
    print(response.text)


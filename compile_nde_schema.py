import json
import os

# location for the combined schema to be saved
output_file = "combined_schema_DO_NOT_EDIT/NIAID_schema.json"

# dictionary to hold the entire schema
schema = {
    "@context": {
        "owl": "http://www.w3.org/2002/07/owl#",
        "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "schema": "http://schema.org/",
        "bioschemas": "https://discovery.biothings.io/view/bioschemas/",
        "niaid": "https://discovery.biothings.io/view/niaid/"
    },
    "@id": "https://discovery.biothings.io/view/niaid/",
    "@graph": []
}

# list all the files in the current working directory
files = os.listdir()

# loop over the files, and append the `@graph` list to the `@graph` object in the schema holder
for filename in files:
    if(".json" in filename):
        with open(filename) as json_file:
            s = json.load(json_file)
            schema["@graph"].extend(s["@graph"])

# Write the full schema to file
with open(output_file, 'w') as f:
    json.dump(schema, f)

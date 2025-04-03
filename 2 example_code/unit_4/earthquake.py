import json

# Load data from JSON file
with open('all_month.geojson', 'r') as file:
    data = json.load(file)

# data now contains the nested dictionary
print(data['features'][0])
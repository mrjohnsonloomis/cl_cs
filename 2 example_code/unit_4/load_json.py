import json

filename = 'temperature_dictionary.json'
with open(filename, 'r') as file:
    temperature_data = json.load(file)
    print(type(temperature_data)) # prints <class 'dict'>
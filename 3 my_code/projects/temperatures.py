# Read the file content into a list
with open('MaxTemps2023.csv', 'r') as file:
    lines = file.readlines()

# Lists to store maximum temperatures
max_temps_phoenix = []
max_temps_hartford = []

# Skip the first line (header) and process the rest
for line in lines[1:]:
    components = line.strip().split(',')
    max_temps_phoenix.append(float(components[1]))
    max_temps_hartford.append(float(components[2]))

# Now max_temps_phoenix and max_temps_hartford lists are ready to be used

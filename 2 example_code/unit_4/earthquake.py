import json
import matplotlib.pyplot as plt

# Load data from JSON file
with open('all_month.geojson', 'r') as file:
    data = json.load(file)

# data now contains the nested dictionary
#print(data)
print(data['features'][0])

#Visualization --- fun fun fun

# Creating sample data
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 4, 1, 7, 6, 8, 3, 5, 9, 4]

# Create the scatterplot
plt.scatter(x, y)

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('My First Scatterplot')

# Display the plot
plt.show()

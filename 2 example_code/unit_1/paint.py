# Program to calculate amount of paint needed
import math
# need to know: total area of wall and coverage per gallon

length = 10
width = 12
height = 10

# Calculate total wall area (Excluding ceiling)

wall_area = 2 * (length + width) * height

# Assumption --> one gallon covers 350 square feet
coverage_per_gallon = 350

# Calcuate gallons needed (math.ceil() rounds up)
gallons_needed = math.ceil(wall_area / coverage_per_gallon)

# Calculate total cost
cost_per_gallon = 50

# Display results
print(f'Gallons of paint needed {gallons_needed}')
print(f'Total estimated cost: ${gallons_needed * cost_per_gallon}')


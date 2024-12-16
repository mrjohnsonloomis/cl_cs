# Problem 1: Game Score Tracker
# Start with the initial week of scores
scores = [85, 92, 78, 90, 88, 95, 89]
print(f'Last week\'s scores: {scores}')

# Add today's new score and remove oldest
new_score = 93
scores.remove(scores[0])
scores.append(new_score)
print(f'After adding today\'s score: {scores}')

# Find all high scores (above 90)
high_scores = []
for score in scores:
    if score > 90:
        high_scores.append(score)
print(f'High scores: {high_scores}')

# Problem 2: Classroom Seating
# Start with full list of students
students = ['Alex', 'Ben', 'Charlie', 'Diana', 'Emma', 'Frank', 'Grace', 
           'Henry', 'Isabel', 'Jack', 'Kelly', 'Liam', 'Maya', 'Noah', 
           'Olivia', 'Pete']
print(f'All students: {students}')

# Set the size for each group
group_size = 3

# Calculate how many complete groups we can make
number_of_complete_groups = len(students) // group_size

# Create groups using a range-based loop
for i in range(number_of_complete_groups):
    # Calculate where this group starts and ends in the list
    start_index = i * group_size
    end_index = start_index + group_size
    
    # Get the students for this group
    current_group = students[start_index:end_index]
    print(f'Group {i + 1}: {current_group}')

# Find any remaining students who didn't fit in a group
remaining_start = number_of_complete_groups * group_size
if remaining_start < len(students):
    remaining_students = students[remaining_start:]
    print(f'Remaining students: {remaining_students}')




# Problem 3: Inventory Management
# Initial inventory levels for each product
inventory = [15, 8, 12, 4, 6, 3, 9]
print(f'Starting inventory: {inventory}')

# Process one sale of each item
for i in range(len(inventory)):
    inventory[i] = inventory[i] - 1
print(f'Inventory after today\'s sales: {inventory}')

# Create empty list for items running low
low_stock = []

# Check each item's quantity
for item in inventory:
    if item < 5:
        low_stock.append(item)
print(f'Warning - These items need to be reordered (less than 5 in stock): {low_stock}')
# Start with a regular list
student1_scores = [95, 88, 92, 85]
print("One student's scores:", student1_scores)
print("First score:", student1_scores[0])
print()

# Now see how a 2D list holds multiple lists
class_scores = [
    [95, 88, 92, 85],     # Student 1 has 4 scores
    [89, 90, 85],         # Student 2 has 3 scores
    [93, 87, 91, 88, 82]  # Student 3 has 5 scores
]
print("All class scores:", class_scores)
print()

# Show how to access elements one at a time
print("Getting specific scores:")
print("First student's first score:", class_scores[0][0])   # 95
print("Second student's last score:", class_scores[1][2])   # 85
print("Third student's fourth score:", class_scores[2][3])  # 88
print()

# Print each student's scores using a basic for loop
print("Printing each student's scores:")
for i in range(len(class_scores)):
    print("Student", i + 1, "scores:", class_scores[i])
print()

# Calculate each student's average using basic loops
print("Calculating averages:")
for i in range(len(class_scores)):
    # Get one student's scores
    student_scores = class_scores[i]
    # Calculate their average
    total = 0
    for j in range(len(student_scores)):
        total = total + class_scores[i][j]
    average = total / len(student_scores)
    
    print("Student", i + 1, "average:", average)
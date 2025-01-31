# Starting data
scores = [88, 92, 75, 95, 83, 77, 91, 82]

# Part 1: Transform these into list comprehensions
# Finding passing scores (≥ 80)
passing = []
for score in scores:
    if score >= 80:
        passing.append(score)

# Adding 2 bonus points to each score
adjusted = []
for score in scores:
    adjusted.append(score + 2)

# Part 2: Transform these into ternary operators
# Grading statement
score = 85  # Example score to test with
if score >= 90:
    result = "A"
else:
    result = "B"

# Class performance check
if len(passing) > 5:
    status = "Excellent class performance"
else:
    status = "Need review session"

# Solutions
'''Expected output with original code:
Original passing scores: [88, 92, 95, 83, 91, 82]
Adjusted scores: [90, 94, 77, 97, 85, 79, 93, 84]
Grade result: B
Class status: Excellent class performance
'''
# After transformation, the code should look like:
passing = [score for score in scores if score >= 80]
adjusted = [score + 2 for score in scores]
result = "A" if score >= 90 else "B"
status = "Excellent class performance" if len(passing) > 5 else "Need review session"
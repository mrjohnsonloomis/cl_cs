def calculate_total(prices):
    # Calculate initial total
    total = 0
    for price in prices:
        total = total + price
    
    # Apply discounts based on total
    if total > 200:
        total = total * 0.8  # 20% off
    elif total > 100:
        total = total * 0.9  # 10% off 
         
    return total


def analyze_temperatures(temperatures):
    # Find highest and lowest temperatures
    highest = temperatures[0]  # Start with first temperature
    lowest = temperatures[0]   # Start with first temperature
    hot_days = 0
    
    for temp in temperatures:
        # Check if this is highest or lowest
        if temp > highest:
            highest = temp
        if temp < lowest:
            lowest = temp
        
        # Count hot days
        if temp > 30:
            hot_days = hot_days + 1
    
    return highest, lowest, hot_days


def process_grades(grades):
    # Calculate the sum for average
    total = 0
    for grade in grades:
        total = total + grade
    
    # Calculate average
    average = total / len(grades)
    
    # Find highest grade
    highest = grades[0]
    for grade in grades:
        if grade > highest:
            highest = grade
    
    # Determine message
    if average > 90:
        message = "Excellent work!"
    elif average >= 80:
        message = "Good job!"
    elif average >= 70:
        message = "Keep practicing!"
    else:
        message = "Let's get some help."
    
    # Round average to one decimal place
    average = round(average, 1)
    
    return average, highest, message


def update_high_scores(scores, new_score):
    # Create a new list to store updated scores
    new_scores = []
    
    # Keep track of whether we've added the new score
    added_new_score = False
    
    # Go through each score in the current list
    for score in scores:
        # If we haven't added the new score yet and it's higher than
        # the current score, add it first
        if not added_new_score and new_score > score:
            new_scores.append(new_score)
            added_new_score = True
        
        # Add the current score from the original list
        new_scores.append(score)
    
    # If we haven't added the new score yet and there's room in the list
    # (less than 5 scores), add it at the end
    if not added_new_score and len(new_scores) < 5:
        new_scores.append(new_score)
    
    # Keep only the top 5 scores
    return new_scores[:5]

#test the functions down here

print(calculate_total([100, 25, 10.99]))
print(calculate_total([10.23, 25.54, 10.99]))

print(analyze_temperatures([32, 33, 56, 38, 35, 32, 28]))

print()

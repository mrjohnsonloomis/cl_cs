# Problem 1: Population Growth Tracker
counts = [100, 150, 180, 205, 400, 800]
first_count = counts[0]
double_count = first_count * 2
hour_found = 0

for hour in range(len(counts)):
    if counts[hour] >= double_count:
        hour_found = hour
        break

print(f"Population doubled at hour: {hour_found}")

# Problem 2: Missing Number Detector
numbers = [1, 2, 3, 4, 6, 7, 8, 9, 10]
missing_number = 0

for num in range(1, 11):  # We know numbers go from 1 to 10
    if num not in numbers:
        missing_number = num
        break

print(f"The missing number is: {missing_number}")

# Problem 3: Vote Counter
votes = [1, 2, 2, 1, 1, 2, 2, 1, 1, 2]
total_votes = len(votes)
yes_votes = 0

for vote in votes:
    if vote == 1:
        yes_votes += 1

no_votes = total_votes - yes_votes

if yes_votes > total_votes/2:
    print("Yes wins!")
elif no_votes > total_votes/2:
    print("No wins!")
else:
    print("No winner - it's a tie!")

# Problem 4: Number Neighbors
numbers = [5, 6, 8, 9, 1, 3, 4, 7]
friendly_pairs = 0

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if (numbers[i] - numbers[j]) == 1:
            friendly_pairs += 1

print(f"Found {friendly_pairs} friendly pairs")
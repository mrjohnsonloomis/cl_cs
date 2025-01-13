# Problem 1: Temperature Alert System
print("\n=== Temperature Alert System ===")

# Initial temperatures
temperatures = [-2, 0, 1, -5, -8, -10, -12, -9]
print("Hourly temperatures:", temperatures)

# Find big temperature drops
big_drops = []
for i in range(1, len(temperatures)):
    if temperatures[i] - temperatures[i-1] < -3:
        big_drops.append(i)
print("Big temperature drops occurred after hours:", big_drops)

# Count dangerous temperatures
danger_count = 0
for i in range(len(temperatures)):
    if temperatures[i] < -10:
        danger_count += 1
print("Number of dangerous readings:", danger_count)

# Print alerts for each temperature
for i in range(len(temperatures)):
    current_temp = temperatures[i]
    if current_temp < -10:
        alert = "DANGER"
    elif current_temp <= -5:
        alert = "WARNING"
    else:
        alert = "SAFE"
    print(f"Hour {i+1}: {alert}")


# Problem 2: Library Book Tracker
print("\n=== Library Book Tracker ===")

# Initial shelf data
shelves = [12, 15, 8, 20, 10, 7, 13, 18]
MAX_BOOKS = 15
print("Current shelf status:", shelves)

# Find overfilled shelves
overfilled = []
for i in range(len(shelves)):
    if shelves[i] > MAX_BOOKS:
        overfilled.append(i)
print("Overfilled shelves:", overfilled)

# Calculate books to move
total_to_move = 0
for i in range(len(shelves)):
    if shelves[i] > MAX_BOOKS:
        total_to_move += shelves[i] - MAX_BOOKS
print("Total books to move:", total_to_move)

# Show available space
print("Shelves with space available:")
for i in range(len(shelves)):
    if shelves[i] < MAX_BOOKS:
        space = MAX_BOOKS - shelves[i]
        print(f"Shelf {i}: Can add {space} books")


# Problem 3: Message Decoder
print("\n=== Message Decoder ===")

# Initial message
message = ['hello', '123', 'world', '456', 'python', '789']
print("Original message:", message)

# Remove elements with numbers
cleaned_message = []
for i in range(len(message)):
    if not message[i].isdigit():
        cleaned_message.append(message[i])
print("Cleaned message:", cleaned_message)

# Count letters in each word
letter_counts = []
for i in range(len(cleaned_message)):
    letter_counts.append(len(cleaned_message[i]))
print("Letter counts:", letter_counts)

# Create repeated words list
decoded_message = []
for i in range(len(cleaned_message)):
    word = cleaned_message[i]
    count = letter_counts[i]
    for j in range(count):
        decoded_message.append(word)
print("Decoded message:", decoded_message)


# Problem 4: Train Station Manager
print("\n=== Train Station Manager ===")

# Initial train times
trains = [1245, 815, 1130, 925, 1428, 1055]
print("All arrivals:", trains)

# Order times
ordered_trains = trains.copy()
ordered_trains.sort()
print("Ordered arrivals:", ordered_trains)

# Separate morning and afternoon
morning_trains = []
afternoon_trains = []
for i in range(len(ordered_trains)):
    if ordered_trains[i] < 1200:
        morning_trains.append(ordered_trains[i])
    else:
        afternoon_trains.append(ordered_trains[i])
print("Morning trains:", morning_trains)
print("Afternoon trains:", afternoon_trains)

# Calculate gaps between trains
print("Time between trains (minutes):")
for i in range(len(ordered_trains) - 1):
    current_time = ordered_trains[i]
    next_time = ordered_trains[i + 1]
    
    # Convert times to minutes for calculation
    current_minutes = (current_time // 100 * 60) + (current_time % 100)
    next_minutes = (next_time // 100 * 60) + (next_time % 100)
    
    gap = next_minutes - current_minutes
    print(f"{current_time} to {next_time}: {gap}")
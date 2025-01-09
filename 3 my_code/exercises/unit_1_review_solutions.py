# Python Review Problems - Solutions
# Note: These solutions avoid using built-in functions like max(), min(), sorted()
# to demonstrate fundamental programming concepts

# Problem 1: Grade Analyzer
print("\n--- Problem 1: Grade Analyzer ---")
scores = [88, 92, 79, 93, 85, 82, 90, 89, 75, 87]

# Initialize with first score
highest = scores[0]
lowest = scores[0]
above_90 = 0

# Single loop to find highest, lowest, and count above 90
for score in scores:
   if score > highest:
       highest = score
   if score < lowest:
       lowest = score
   if score > 90:
       above_90 += 1

score_range = highest - lowest

print("All scores:", scores)
print("Highest score:", highest)
print("Lowest score:", lowest) 
print("Score range:", score_range)
print("Number of scores above 90:", above_90)

# Problem 2: Playlist Manager
print("\n--- Problem 2: Playlist Manager ---")
playlist = ['song1', 'song2', 'song3', 'song1', 'song4', 'song2', 'song5']

# Remove duplicates while preserving order
unique_playlist = []
for song in playlist:
   if song not in unique_playlist:
       unique_playlist.append(song)

# Find longest song name
longest_song = unique_playlist[0]
for song in unique_playlist[1:]:
   if len(song) > len(longest_song):
       longest_song = song

# Create new list with longest first
final_playlist = [longest_song]
for song in unique_playlist:
   if song != longest_song:
       final_playlist.append(song)

print("Original playlist:", playlist)
print("Playlist without duplicates:", unique_playlist)
print("Final playlist (longest song first):", final_playlist)
print("Number of songs:", len(unique_playlist))

# Problem 3: Word Analyzer
print("\n--- Problem 3: Word Analyzer ---")
languages = ['python', 'javascript', 'java', 'ruby', 'golang', 'scala']

# Find longest and shortest without max/min
longest = languages[0]
shortest = languages[0]
for lang in languages:
   if len(lang) > len(longest):
       longest = lang
   if len(lang) < len(shortest):
       shortest = lang

# Find words containing 'a'
contains_a = []
for lang in languages:
   if 'a' in lang:
       contains_a.append(lang)

# Order by length (bubble sort implementation)
ordered = languages.copy()
for i in range(len(ordered)):
   for j in range(len(ordered) - 1):
       if len(ordered[j]) > len(ordered[j + 1]):
           ordered[j], ordered[j + 1] = ordered[j + 1], ordered[j]

print("All languages:", languages)
print("Longest word:", longest)
print("Shortest word:", shortest)
print("Words containing 'a':", contains_a)
print("Ordered by length:", ordered)

# Problem 4: Number Sequence Analyzer
print("\n--- Problem 4: Number Sequence Analyzer ---")
numbers = [4, 8, 15, 16, 23, 42, 108]

# Find numbers divisible by both 2 and 3
divisible_by_both = []
for num in numbers:
   if num % 2 == 0 and num % 3 == 0:
       divisible_by_both.append(num)

# Find numbers between 15 and 50
between = []
for num in numbers:
   if 15 <= num <= 50:
       between.append(num)

# Calculate average without sum()
total = 0
for num in numbers:
   total += num
average = total / len(numbers)

print("Original sequence:", numbers)
print("Divisible by 2 and 3:", divisible_by_both)
print("Numbers between 15 and 50:", between)
print("Average of all numbers:", average)

# Problem 5: Text Adventure Inventory
print("\n--- Problem 5: Text Adventure Inventory ---")
inventory = ['sword', 'shield', 'potion', 'potion', 'arrow', 'arrow', 'arrow']

# Count items without using count()
item_counts = []
unique_items = []

# Get unique items first
for item in inventory:
   if item not in unique_items:
       unique_items.append(item)

# Count occurrences of each unique item
for unique_item in unique_items:
   count = 0
   for item in inventory:
       if item == unique_item:
           count += 1
   item_counts.append(count)

print("Current inventory:", inventory)
print("Inventory summary:")
for i in range(len(unique_items)):
   print(f"- {unique_items[i]}: {item_counts[i]}")
print("Unique items:", unique_items)
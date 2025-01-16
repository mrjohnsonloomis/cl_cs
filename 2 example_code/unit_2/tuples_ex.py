# Create a tuple of coordinates (x, y)
point = (10, 20)

# Method 1: Unpacking the tuple into separate variables
x, y = point

print("Using tuple unpacking:")
print("x:", x)
print("y:", y)

# Method 2: Using bracket notation (indexing)
# Remember: index starts at 0, so first value is at index 0
print("\nUsing bracket notation:")
print("x:", point[0])    # Gets the first value (index 0)
print("y:", point[1])    # Gets the second value (index 1)

# Let's do a more complex example with a book tuple
book = ("The Hobbit", 1937, "J.R.R. Tolkien")

# Method 1: Unpacking into meaningful variable names
title, year, author = book

print("\nBook information using unpacking:")
print("Title:", title)
print("Year:", year)
print("Author:", author)

# Method 2: Using bracket notation
print("\nBook information using bracket notation:")
print("Title:", book[0])     # First element
print("Year:", book[1])      # Second element
print("Author:", book[2])    # Third element
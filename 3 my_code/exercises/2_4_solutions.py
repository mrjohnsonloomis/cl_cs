"""
Library System - Dictionary Practice Solutions
This script contains solutions to all three library system practice problems.
Each solution demonstrates different ways to work with Python dictionaries.
"""

# ===== Problem 1: Book Status Tracker =====
print("\nProblem 1: Book Status Tracker")
print("=" * 40)

# Create a dictionary of books and their status
book_status = {
    "The Hobbit": True,    # True means checked out
    "Dune": False,         # False means available
    "Foundation": True,
    "1984": False
}

# Print all book titles
print("All books:", list(book_status.keys()))

# Find available books (where value is False)
available_books = []
# Loop through each entry in the dictionary one at a time
for entry in book_status.items():
    # entry[0] is the book title, entry[1] is the checkout status
    if not entry[1]:  # if not checked out
        available_books.append(entry[0])  # add the book title
print("Available books:", available_books)

# Count checked out books (where value is True)
checked_out_count = 0
# Loop through just the values (the True/False status)
for status in book_status.values():
    if status:  # if checked out (True)
        checked_out_count = checked_out_count + 1
print("Number of books checked out:", checked_out_count)

# ===== Problem 2: Book Borrower System =====
print("\nProblem 2: Book Borrower System")
print("=" * 40)

# Create dictionary of books and borrowers
book_borrowers = {
    "The Hobbit": "Sarah Johnson",
    "Dune": None,
    "Foundation": "Patricia Brown",
    "1984": None
}

# Print status of each book
print("Book status:")
# Loop through each entry in the dictionary
for entry in book_borrowers.items():
    # entry[0] is the book title, entry[1] is the borrower name
    book_title = entry[0]
    borrower_name = entry[1]
    
    if borrower_name is None:
        print(f"{book_title} - available")
    else:
        print(f"{book_title} - borrowed by {borrower_name}")

# Find Sarah's books
sarahs_books = []
# Loop through each entry to find Sarah's books
for entry in book_borrowers.items():
    # entry[0] is the book title, entry[1] is the borrower name
    if entry[1] == "Sarah Johnson":
        sarahs_books.append(entry[0])
print("\nSarah Johnson has these books:", sarahs_books)

# Find available books
available_books = []
# Loop through each entry to find available books
for entry in book_borrowers.items():
    # entry[0] is the book title, entry[1] is the borrower name
    if entry[1] is None:
        available_books.append(entry[0])
print("Available books:", available_books)

# ===== Problem 3: Book Counter =====
print("\nProblem 3: Book Counter")
print("=" * 40)

# Create dictionary of borrow counts
times_borrowed = {
    "The Hobbit": 25,
    "Dune": 28,
    "Foundation": 15,
    "1984": 32
}

# Find most popular book
most_borrowed = max(times_borrowed.values())
# Loop through to find which book matches this number
for entry in times_borrowed.items():
    # entry[0] is the book title, entry[1] is the number of times borrowed
    if entry[1] == most_borrowed:
        print(f"Most popular book: {entry[0]} ({entry[1]} times)")

# Find books borrowed less than 20 times
less_popular = []
for entry in times_borrowed.items():
    # entry[0] is the book title, entry[1] is the number of times borrowed
    if entry[1] < 20:
        less_popular.append(entry[0])
print("Books borrowed less than 20 times:", less_popular)

# Calculate average times borrowed
total_borrows = sum(times_borrowed.values())
average_borrows = total_borrows / len(times_borrowed)
print("Average times borrowed:", average_borrows)
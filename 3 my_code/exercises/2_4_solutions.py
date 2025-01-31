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
for book, is_checked_out in book_status.items():
    if not is_checked_out:
        available_books.append(book)
print("Available books:", available_books)

# Count checked out books (where value is True)
checked_out_count = 0
for status in book_status.values():
    if status:
        checked_out_count += 1
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
for book, borrower in book_borrowers.items():
    if borrower is None:
        print(f"{book} - available")
    else:
        print(f"{book} - borrowed by {borrower}")

# Find Sarah's books
sarahs_books = []
for book, borrower in book_borrowers.items():
    if borrower == "Sarah Johnson":
        sarahs_books.append(book)
print("\nSarah Johnson has these books:", sarahs_books)

# Find available books
available_books = []
for book, borrower in book_borrowers.items():
    if borrower is None:
        available_books.append(book)
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
for book, times in times_borrowed.items():
    if times == most_borrowed:
        print(f"Most popular book: {book} ({times} times)")

# Find books borrowed less than 20 times
less_popular = []
for book, times in times_borrowed.items():
    if times < 20:
        less_popular.append(book)
print("Books borrowed less than 20 times:", less_popular)

# Calculate average times borrowed
total_borrows = sum(times_borrowed.values())
average_borrows = total_borrows / len(times_borrowed)
print("Average times borrowed:", average_borrows)
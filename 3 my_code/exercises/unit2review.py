"""
A set of solutions for the Python practice problems for Unit 2 Review.
"""

# Problem 1: Functions & Modular Programming
def is_valid_discount(d: float) -> bool:
    """
    Check if the discount is between 0 and 100 (inclusive).
    """
    return 0 <= d <= 100

def calculate_discount(price: float, discount: float) -> float:
    """
    Compute the discounted price if the discount is valid.
    If the discount is not valid, return False to indicate an error.
    """
    if not is_valid_discount(discount):
        return False  # Signal invalid discount
    return price - (price * discount / 100)

# Problem 2: Dictionary Explorer
def grade_evaluation(grades: dict) -> None:
    print("Student names:", grades.keys())
    print("Scores:", grades.values())
    print("Student items:", grades.items())
    for student, score in grades.items():
        # Use ternary operator for pass/fail
        status = "Pass" if score >= 60 else "Fail"
        print(f"{student}: {status}")


# Problem 3: Tuple Unpacking for Coordinates
def process_coordinate(coord: tuple) -> tuple:
    x, y, z = coord  # tuple unpacking
    print(f"x = {x}")
    print(f"y = {y}")
    print(f"z = {z}")
    # Return a new tuple with each coordinate multiplied by 2
    return (x * 2, y * 2, z * 2)


# Problem 4: List Comprehension to Square Numbers
def square_numbers(nums: list) -> list:
    return [num ** 2 for num in nums]


# Problem 5: Ternary Operator in a Function
def even_or_odd(n: int) -> str:
    return "Even" if n % 2 == 0 else "Odd"


# Problem 6: Combining Dictionaries and List Comprehensions
def student_pass_fail(data: list) -> dict:
    # Using dictionary comprehension
    return {name: ("Pass" if score >= 60 else "Fail") for name, score in data}


# Problem 7: Advanced Modular Program: Grade Statistics
def max_score(scores: list) -> int:
    return max(scores) if scores else 0

def min_score(scores: list) -> int:
    return min(scores) if scores else 0

def average_score(scores: list) -> float:
    return sum(scores) / len(scores) if scores else 0.0

def grade_statistics(students: list) -> dict:
    # Use list comprehension to extract scores from the list of dictionaries
    scores = [student["score"] for student in students]
    return {
        "max": max_score(scores),
        "min": min_score(scores),
        "average": average_score(scores)
    }

# Main block for demonstration purposes
def main():
    # Problem 1 demonstration
    price = float(input("Enter price: "))
    
    # Get a valid discount using a loop with a condition
    discount = float(input("Enter discount percentage (0-100): "))
    while not is_valid_discount(discount):
        print("Invalid discount. Please enter a discount percentage between 0 and 100.")
        discount = float(input("Enter discount percentage (0-100): "))
    
    result = calculate_discount(price, discount)
    print(f"Discounted price is: {result}")

    print("\n--- Problem 2 ---")
    students_grades = {"Alice": 85, "Bob": 55, "Charlie": 60}
    grade_evaluation(students_grades)

    print("\n--- Problem 3 ---")
    new_coord = process_coordinate((1, 2, 3))
    print(new_coord)

    print("\n--- Problem 4 ---")
    squared = square_numbers([1, 2, 3, 4])
    print(squared)

    print("\n--- Problem 5 ---")
    print(even_or_odd(7))
    print(even_or_odd(10))

    print("\n--- Problem 6 ---")
    student_data = [("Alice", 90), ("Bob", 45), ("Charlie", 75)]
    print(student_pass_fail(student_data))

    print("\n--- Problem 7 ---")
    student_list = [
        {"name": "Alice", "score": 88},
        {"name": "Bob", "score": 72},
        {"name": "Charlie", "score": 95},
        {"name": "Diana", "score": 60}
    ]
    stats = grade_statistics(student_list)
    print(stats)
main()
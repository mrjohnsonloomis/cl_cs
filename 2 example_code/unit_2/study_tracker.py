# This program demonstrates list comprehensions, ternary operators, and input validation
# by creating a simple study hour tracker

def get_valid_hours():
    """Get valid study hours from user with simple input validation.
      Just checking for range of ints"""
    hours = 0

    user_input = int(input("How many hours did you study today? "))
    # A valid input is a number between 0 and 24
    while user_input <= 0 or user_input >=24:
        user_input = int(input("Hm. Not valid input. How many hours did you study today? "))
    hours = user_input
    return hours

def analyze_study_data(hours_list):
    """Analyze study data using list comprehension"""
    
    # List comprehension to identify "good study days" (>= 2 hours)
    good_study_days = [day for day in range(len(hours_list)) 
                      if hours_list[day] >= 2]
    
    return good_study_days

def main():
    # Track 5 days of study hours
    study_hours = []
    
    print("Let's track your study hours for 5 days!")
    for day in range(5):
        print(f"\nDay {day + 1}:")
        hours = get_valid_hours()
        print('here')
        study_hours.append(hours)
    
    # Analyze the data
    good_days = analyze_study_data(study_hours)
    
    # Display results
    print("\nStudy Analysis:")
    print(f"Your study hours: {study_hours}")
    print(f"Days with good study habits (>= 2 hours): Day {[day + 1 for day in good_days]}")
    
    print("\nDaily Ratings:")
   
    # Use a ternary operator to give overall feedback
    avg_hours = sum(study_hours) / len(study_hours)
    overall = "Great job!" if avg_hours >= 3 else "Keep working on building those study habits!"
    print(f"\n{overall}")


main()
# student IDs

def create_student_id(grade, first_initial, last_name):
    """Creates a student ID from grade, first initial, and last name"""
    # Pad grade with leading zero if needed
    grade_str = str(grade)
    if grade < 10:
        grade_str = "0" + grade_str
    
    # Truncate last name if longer than 5 characters
    if len(last_name) > 5:
        last_name = last_name[0:5]
    
    # Combine and convert to uppercase
    student_id = grade_str + first_initial + last_name
    return student_id.upper()

# Test the function
grade = 7
first_name = "John"
last_name = "Smith"
print("Student info: Grade", int(grade) + ",", first_name, last_name)
print("Student ID:", create_student_id(grade, first_name[0], last_name))
print()

grade = 12
first_name = "Alexandra"
last_name = "Rodriguez"
print("Student info: Grade", grade + ",", first_name, last_name)
print("Student ID:", create_student_id(grade, first_name[0], last_name))


# Temperature reading

def get_fahrenheit(temp_string):
    """Extracts the Fahrenheit temperature from a temperature string"""
    f_part = temp_string.split("/")
    f_part = f_part[0]
    f_part = int(f_part.replace("F", ""))
    return f_part

def get_celsius(temp_string):
    """Extracts the Celsius temperature from a temperature string"""
    c_part = temp_string.split("/")[1]
    return int(c_part.replace("C", ""))

def find_highest_temp(temp_list):
    """Finds the highest Fahrenheit temperature in a list of readings"""
    highest = 0
    for temp in temp_list:
        current_temp = get_fahrenheit(temp)
        if current_temp > highest:
            highest = current_temp
    return str(highest) + "F"

# Test the functions
temperatures = ['75F/24C', '68F/20C', '82F/28C', '71F/22C']
print("Temperature readings:", temperatures)
print("Fahrenheit from first reading:", get_fahrenheit(temperatures[0]))
print("Celsius from first reading:", get_celsius(temperatures[0]))
print("Highest temperature:", find_highest_temp(temperatures))
# Word Scrambler


def reverse_word(word):
    """Takes a word and returns it reversed"""
    reversed_word = ""
    for letter in word:
        reversed_word = letter + reversed_word
    return reversed_word

def scramble_sentence(sentence):
    """Takes a sentence and returns it with each word reversed"""
    words = sentence.split()
    scrambled_words = []
    for word in words:
        scrambled_word = reverse_word(word)
        scrambled_words.append(scrambled_word)
    return " ".join(scrambled_words)

# Test the functions
word = "python"
print("Original word:", word)
print("Scrambled word:", reverse_word(word))
print()

sentence = "have a nice day"
print("Original sentence:", sentence)
print("Scrambled sentence:", scramble_sentence(sentence))
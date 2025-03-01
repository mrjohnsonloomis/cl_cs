# Part a: make_password function
# This function prompts the user for a sentence and returns a password made up of the first letter of each word.
# It repeats asking (using a while loop with a condition) until the password is at least 7 characters long.
def make_password():
    valid = False
    password = ""
    while not valid:
        sentence = input("Enter your password sentence: ")
        words = sentence.split()
        password = ""
        for word in words:
            password += word[0]
        if len(password) >= 7:
            valid = True
        else:
            print("Password must be at least 7 characters long. Please try again.")
    return password


# Part b: login function
# This function prompts the user for their username and a password (using make_password).
# If the username does not exist in user_data, it creates a new entry and logs them in.
# If the username exists, it checks whether the entered password matches the user's current password.
# It returns a tuple: (True/False for successful login, username)
def login(user_data):
    username = input("Enter your username: ")
    password = make_password()
    
    if username not in user_data:
        user_data[username] = [password]
        print("New user created and logged in.")
        return True, username
    else:
        current_password = user_data[username][-1]
        if password == current_password:
            print("Logged in successfully.")
            return True, username
        else:
            print("Incorrect password. Login failed.")
            return False, username


# Part c: Code for logging in a user and prompting them to change their password if login is successful.
# This part uses the login function above, and then asks the user for a new password.
# It ensures that the new password is not one of the user's previous passwords.
user_data = {
    'kseyboth': ['csitbse', 'qrahruteot', 'iasrfsbicsi'],
    'mjohnson': ['aiigtre', 'siltsuanr'],
    'smacclintic': ['ttgistgtist']
}

logged_in, user = login(user_data)

if logged_in:
    print("It is time to change your password.")
    change_valid = False
    while not change_valid:
        new_password = make_password()
        if new_password in user_data[user]:
            print("You cannot reuse an old password. Try a different sentence.")
        else:
            user_data[user].append(new_password)
            print("Password changed successfully.")
            change_valid = True

print("Final user data:", user_data)

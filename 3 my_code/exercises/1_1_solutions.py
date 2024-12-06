#1
# Get temperature input from user
temperature = float(input("What is the temperature in Fahrenheit? "))

# Check temperature and provide appropriate advice
if temperature < 60:
    print("You should wear a jacket today!")
else:
    print("No jacket needed today!")

#2
# Get the original price from user
original_price = float(input("Enter the original price: "))

# Calculate discount based on price
if original_price >= 100:
    discount = 0.20  # 20% discount
    final_price = original_price * (1 - discount)
    print(f"Your final price after the 20% discount is: ${final_price}")
else:
    discount = 0.10  # 10% discount
    final_price = original_price * (1 - discount)
    print(f"Your final price after the 10% discount is: ${final_price}")

#3

# Get income and expense from user
monthly_income = float(input("What is your monthly income? "))
expense = float(input("Enter the expense amount: "))

# Calculate percentage of income
expense_percentage = (expense / monthly_income) * 100

# Determine expense category
if expense_percentage < 10:
    print("This expense is Low - it's less than 10% of your income.")
elif expense_percentage <= 25:
    print("This expense is Moderate - it's between 10% and 25% of your income.")
else:
    print("This expense is High - it's more than 25% of your income.")
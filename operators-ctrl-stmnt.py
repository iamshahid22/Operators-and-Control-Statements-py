# Working with Operators and Control Statements in Python

# 1. Function to compare two numbers
def compare_numbers(num1, num2):
    if num1 > num2:
        print(f"{num1} is larger than {num2}")
    elif num2 > num1:
        print(f"{num2} is larger than {num1}")
    else:
        print("Both numbers are equal")


# 2. Logical Operators

def check_number_range(number):
    if number >= 10 and number <= 20:
        print(f"{number} is within the range 10 to 20")
    else:
        print(f"{number} is outside the range 10 to 20")


def check_string(text):
    if text != "" and len(text) > 5:
        print("String is not empty and length is greater than 5")
    else:
        print("Condition not satisfied")


# 3. Simple Calculator

def calculator(num1, num2, operation):
    if operation == "+":
        print("Result:", num1 + num2)
    elif operation == "-":
        print("Result:", num1 - num2)
    elif operation == "*":
        print("Result:", num1 * num2)
    elif operation == "/":
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Cannot divide by zero")
    else:
        print("Invalid operation")


# 4. Age Classification

def classify_age(age):
    if age < 13:
        print("Category: Child")
    elif age < 20:
        print("Category: Teenager")
    elif age < 60:
        print("Category: Adult")
    else:
        print("Category: Senior")


# 5. Simple Login System

def login_system(username, password):
    valid_username = "admin"
    valid_password = "12345"

    if username == valid_username and password == valid_password:
        print("Login Successful")
    else:
        print("Invalid Username or Password")


# ----------------------------
# Function Calls (Testing)
# ----------------------------

compare_numbers(15, 25)

check_number_range(15)

check_string("Python")

calculator(20, 10, "+")

classify_age(18)

login_system("admin", "12345")

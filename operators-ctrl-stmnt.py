# 1. Comparison Operators - Find Larger Number

def find_larger(num1, num2):
    if num1 > num2:
        print(f"{num1} is larger than {num2}")
    elif num2 > num1:
        print(f"{num2} is larger than {num1}")
    else:
        print("Both numbers are equal")


# Example
find_larger(15, 25)


# 2. Logical Operators

# Check if a number is within the range 10 to 20
number = 15

if number >= 10 and number <= 20:
    print(f"{number} is within the range 10 to 20")
else:
    print(f"{number} is not within the range 10 to 20")


# Check if a string is not empty and length is greater than 5
text = "Python"

if text and len(text) > 5:
    print("String is not empty and length is greater than 5")
else:
    print("Condition not satisfied")


# 3. Simple Calculator using Conditional Statements

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operation (+, -, *, /): ")

if operator == "+":
    print("Result =", num1 + num2)

elif operator == "-":
    print("Result =", num1 - num2)

elif operator == "*":
    print("Result =", num1 * num2)

elif operator == "/":
    if num2 != 0:
        print("Result =", num1 / num2)
    else:
        print("Division by zero is not allowed")

else:
    print("Invalid operator")


# 4. Age Classification

age = int(input("Enter your age: "))

if age < 13:
    print("Category: Child")

elif age < 20:
    print("Category: Teenager")

elif age < 60:
    print("Category: Adult")

else:
    print("Category: Senior")


# 5. Simple Login System

correct_username = "admin"
correct_password = "12345"

username = input("Enter username: ")
password = input("Enter password: ")

if username == correct_username and password == correct_password:
    print("Login Successful")

else:
    print("Invalid Username or Password")

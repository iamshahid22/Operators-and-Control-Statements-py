# Operators (Comparison and Logical) and Control Statements

# Comparison Operators
a = 15
b = 25

if a > b:
    print(a, "is larger")
elif b > a:
    print(b, "is larger")
else:
    print("Both numbers are equal")

# Logical Operators
num = 15

if num >= 10 and num <= 20:
    print("Number is within the range 10 to 20")
else:
    print("Number is outside the range")

text = "Python"

if text != "" and len(text) > 5:
    print("String is not empty and length is greater than 5")
else:
    print("Condition not satisfied")

# Conditional Statements - Calculator
num1 = 20
num2 = 10
operation = "+"

if operation == "+":
    print("Addition:", num1 + num2)
elif operation == "-":
    print("Subtraction:", num1 - num2)
elif operation == "*":
    print("Multiplication:", num1 * num2)
elif operation == "/":
    if num2 != 0:
        print("Division:", num1 / num2)
    else:
        print("Cannot divide by zero")

# Age Classification
age = 18

if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior")

# Login System
username = "admin"
password = "12345"

entered_username = "admin"
entered_password = "12345"

if entered_username == username and entered_password == password:
    print("Login Successful")
else:
    print("Invalid Credentials")

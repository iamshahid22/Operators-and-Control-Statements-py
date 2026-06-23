# Task 1: Compare Two Integers
def compare_integers(a, b):
    print("--- Task 1 ---")
    if a > b:
        print(f"{a} is larger than {b}")
    elif b > a:
        print(f"{b} is larger than {a}")
    else:
        print(f"{a} and {b} are equal")

# Task 2: Logical Operators
def evaluate_conditions(num, text):
    print("\n--- Task 2 ---")
    is_in_range = 10 <= num <= 20
    print(f"Is {num} between 10 and 20? {is_in_range}")
    is_valid_string = len(text) > 0 and len(text) > 5
    print(f"Is string '{text}' valid? {is_valid_string}")

# Task 3: Simple Calculator
def calculator(op, num1, num2):
    print("\n--- Task 3 ---")
    if op == '+':
        print(f"Result: {num1 + num2}")
    elif op == '-':
        print(f"Result: {num1 - num2}")
    elif op == '*':
        print(f"Result: {num1 * num2}")
    elif op == '/':
        if num2 != 0:
            print(f"Result: {num1 / num2}")
        else:
            print("Error: Division by zero")
    else:
        print("Invalid operator")

# Task 4: Age Classification
def classify_age(age):
    print("\n--- Task 4 ---")
    if age < 0:
        print("Invalid age")
    elif age < 13:
        print("Category: Child")
    elif age < 20:
        print("Category: Teenager")
    elif age < 65:
        print("Category: Adult")
    else:
        print("Category: Senior")

# Task 5: Login System
def login(username, password):
    print("\n--- Task 5 ---")
    stored_user = "admin"
    stored_pass = "secure123"
    if username == stored_user and password == stored_pass:
        print("Login successful!")
    else:
        print("Invalid username or password.")

# Execution
if __name__ == "__main__":
    compare_integers(15, 10)
    evaluate_conditions(15, "HelloPython")
    calculator('+', 10, 5)
    classify_age(25)
    login("admin", "secure123")
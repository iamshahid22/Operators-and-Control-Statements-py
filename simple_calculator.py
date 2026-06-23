def calculator(op, num1, num2):
    if op == '+':
        print(f"Result: {num1 + num2}")
    elif op == '-':
        print(f"Result: {num1 - num2}")
    elif op == '*':
        print(f"Result: {num1 * num2}")
    elif op == '/':
        print(f"Result: {num1 / num2 if num2 != 0 else 'Error: Division by zero'}")
    else:
        print("Invalid operator")

# Example usage:
calculator('+', 10, 5)
# Comparison Operators

def compare_numbers(a, b):
    if a > b:
        print(f"{a} is larger")
    elif a < b:
        print(f"{b} is larger")
    else:
        print("Both numbers are equal")

compare_numbers(10, 20)

# Logical Operators

num = 15

if num >= 10 and num <= 20:
    print("Number is within range")

text = "Python"

if text != "" and len(text) > 5:
    print("Valid string")

# Conditional Statements

age = 18

if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior")

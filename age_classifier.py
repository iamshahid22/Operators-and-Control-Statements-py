def classify_age(age):
    if age < 13:
        print("Category: Child")
    elif age < 20:
        print("Category: Teenager")
    elif age < 65:
        print("Category: Adult")
    else:
        print("Category: Senior")

# Example usage:
classify_age(25)
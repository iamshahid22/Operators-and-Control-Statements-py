def evaluate_conditions(num, text):
    # Check if number is between 10 and 20 (inclusive)
    is_in_range = 10 <= num <= 20
    print(f"Is {num} between 10 and 20? {is_in_range}")

    # Check if string is not empty and length > 5
    is_valid_string = len(text) > 0 and len(text) > 5
    print(f"Is string '{text}' valid? {is_valid_string}")

# Example usage:
evaluate_conditions(15, "HelloPython")
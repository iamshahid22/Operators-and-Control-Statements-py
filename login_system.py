def login(username, password):
    # Hardcoded credentials
    stored_user = "admin"
    stored_pass = "secure123"

    if username == stored_user and password == stored_pass:
        print("Login successful!")
    else:
        print("Invalid username or password.")

# Example usage:
login("admin", "secure123")
def login():
    """
    Function to prompt user for username and password, then checks if credentials are valid.
    """
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Replace with your actual validation logic based on a database or stored credentials
    if username == "admin" and password == "password":
        print("Login successful!")
    else:
        print("Invalid username or password.") 

# Example usage
login()

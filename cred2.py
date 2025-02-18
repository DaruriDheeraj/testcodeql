# Dummy username and password
USERNAME = "admin"
PASSWORD = "password123"

def login():
    # Ask the user for username and password
    user_input_username = input("Enter username: ")
    user_input_password = input("Enter password: ")

    # Check if the entered credentials match the dummy ones
    if user_input_username == USERNAME and user_input_password == PASSWORD:
        print("Login successful!")
    else:
        print("Invalid username or password. Please try again.")

# Call the login function
login()

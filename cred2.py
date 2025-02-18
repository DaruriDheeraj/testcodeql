# Sample Python code with username and password login

# Predefined username and password
correct_username = "admin"
correct_password = "password123"

# Function to handle login
def login():
    # Get user input for username and password
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Check if the entered username and password match the predefined values
    if username == correct_username and password == correct_password:
        print("Login successful!")
    else:
        print("Invalid username or password. Please try again.")

# Call the login function
login()

# script that simulates a **basic user authentication system**.

users = {}  # Dictionary to store usernames and passwords
def register():

    while True:
        print('Are you a New or Existing user?')
        print('Type New, Existing, or Exit: ', end='')
        choice = input().lower()

        if choice == 'new':   # new user registration, passes credentials to def register_user
            print ('\nRegister a New User:')
            username = input("Enter username: ")
            password = input("Enter password: ")
            print(register_user(users, username, password))

        elif choice == 'existing':   # existing user login, passes credentials to def existing_user
            username = input("Enter username: ")
            password = input("Enter password: ")
            print(existing_user(users, username, password))
            break
        elif choice == 'exit':   # exits program
            print("Exiting program. Goodbye!")
            break
        else:  # handles mistyped input requesting new, exisitng, or exit
            print('Please enter New, Existing, or Exit.\n')


def register_user(users, username, password): # function handles new user registration

    if username in users:
        return "Registration failed: Username already exists.\n"
    else:
        users[username] = password
        return "User registered successfully!\n"

def existing_user(users, username, password):  # function handles existing user registration

    if username in users and users[username] == password:
        return "Login successful!\n"
    else:
        return "Login failed: Invalid credentials."

if __name__ == "__main__":  # this statement defines the function that
    register()              # begins the script when opened, begins at def register

"""

CP1404 - Practical 2

Password to asterisks

"""

MIN_LENGTH = 8

def get_password():
    # Ask for password with error-checking
    while True:
        password = input("Enter password: ")
        if len(password) < MIN_LENGTH:
            print("Password must be at least", MIN_LENGTH, "characters long.")
        else:
            return password

def print_password_asterisks(password):
    # Print asterisks as long as the password
    print("*" * len(password))

def main():
    password = get_password()
    print_password_asterisks(password)

if __name__ == '__main__':
    main()
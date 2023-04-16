"""
CP1404/CP5632 Practical
Emails
Estimate: 30 minutes
Actual:   25 minutes
"""

def extract_name(email):
    """
    Given an email, extract the name of the user.
    """
    parts = email.split('@')[0].split('.')
    return ' '.join([part.title() for part in parts])


def email_check():
    # Create an empty dictionary to store the emails and names.
    emails_to_names = {}


    # Ask the user for their email until they enter a blank one.
    email = input("Email: ")
    while email != "":
        name = extract_name(email)
        # Ask the user to confirm the name.
        response = input(f"Is your name {name}? (Y/n) ").strip().lower()

        # If the user doesn't confirm the name, ask for their name.
        if response.lower() == 'n':
            name = input("Name: ")

        # Store the email and name in the dictionary.
        emails_to_names[email] = name

        email = input("Email: ")

    # Loop
    for email, name in emails_to_names.items():
        print(f"{name} ({email})")


email_check()

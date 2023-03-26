"""
CP1404 - Practical 3
Pseudocode for temperature conversion：
set MENU to "C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ - Quit"
display MENU
get choice from user, convert to uppercase

while choice is not "Q":
    if choice is "C":
        get temperature in Celsius from user
        convert temperature to Fahrenheit using formula: fahrenheit = celsius * 9/5 + 32
        display result in Fahrenheit
    else if choice is "F":
        get temperature in Fahrenheit from user
        convert temperature to Celsius using formula: celsius = (fahrenheit - 32) * 5/9
        display result in Celsius
    else:
        display "Invalid option" message

    display MENU
    get choice from user, convert to uppercase

display "Thank you." message
"""


def celsius_to_fahrenheit(celsius):
    # Convert Celsius to Fahrenheit
    return (celsius * 9.0 / 5 + 32)


def fahrenheit_to_celsius(fahrenheit):
    # Convert Fahrenheit to Celsius
    return (5 / 9 * (fahrenheit - 32))


MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""

print(MENU)

choice = input(">>> ").upper()

while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"Result: {fahrenheit:.2f} F")
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"Result: {celsius:.2f} C")
    else:
        #Invalid choice
        print("Invalid option")

    #Display menu again
    print(MENU)
    choice = input(">>> ").upper()

print("Thank you.")

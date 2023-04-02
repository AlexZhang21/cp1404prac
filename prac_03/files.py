# Write user's name to a file
name = input("Enter your name: ")
with open("name.txt", "w") as file:
    file.write(name)

# Read the name from file and print it
with open("name.txt", "r") as file:
    name = file.read()
print(f"Your name is {name}")

# Read the first two numbers from file and print their sum
with open("numbers.txt", "r") as file:
    num1 = int(file.readline())
    num2 = int(file.readline())
print(num1 + num2)

# Print the total for all lines in file
total = 0
with open("numbers.txt", "r") as file:
    for line in file:
        total += int(line)
print(total)

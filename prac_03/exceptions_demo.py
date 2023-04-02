"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    When input is not integer, like 0.01
2. When will a ZeroDivisionError occur?
    When denominator is zero.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    Yes, by asking denominator again if is zero
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Cannot divide by 0")
        denominator = int(input("Enter the denominator: "))
    print(numerator / denominator)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")





#
# try:
#     numerator = int(input("Enter the numerator: "))
#     denominator = int(input("Enter the denominator: "))
#     if denominator == 0:
#         print("Cannot divide by zero!")
#     else:
#         fraction = numerator / denominator
#         print(fraction)
# except ValueError:
#     print("Numerator and denominator must be valid numbers!")
# print("Finished.")
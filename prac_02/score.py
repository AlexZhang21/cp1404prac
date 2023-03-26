"""

CP1404 - Practical 2

Display user score and random score

"""

import random

PASS = 50
EXCELLENT = 90
MAX = 100


def main():
    score = float(input("Enter score: "))
    print(get_score(score))
    # New - Random Result
    ran_score = random_score()
    print(f"Random number= {int(ran_score)} which is {get_score(ran_score)}")


def random_score():
    return random.uniform(0, MAX)


def get_score(score):
    if score < 0 or score > MAX:
        message = "Invalid score"
    elif score >= EXCELLENT:
        message = "Excellent"
    elif score >= PASS:
        message = "Passable"
    else:
        message = "Bad"
    return message

if __name__ == '__main__':
    main()

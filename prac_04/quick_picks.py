import random

NUM_QUICK_PICKS = 5
NUMBERS_PER_PICK = 6
MIN_NUMBER = 1
MAX_NUMBER = 45

#run 5 rounds
for i in range(NUM_QUICK_PICKS):
    numbers = []
    #run 6 numbers
    while len(numbers) < NUMBERS_PER_PICK:
        num = random.randint(MIN_NUMBER, MAX_NUMBER)
        if num not in numbers:
            numbers.append(num)
    numbers.sort()
    #show all nums
    print(" ".join("{:2d}".format(num) for num in numbers))



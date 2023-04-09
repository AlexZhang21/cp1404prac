import random

NUM_QUICK_PICKS = 5
NUMBERS_PER_PICK = 6
MIN_NUMBER = 1
MAX_NUMBER = 45

#get 5 rounds
for i in range(NUM_QUICK_PICKS):
    numbers = []
    #get 6 numbers
    while len(numbers) < NUMBERS_PER_PICK:
        #Get random num between min, max num
        num = random.randint(MIN_NUMBER, MAX_NUMBER)
        #if new number, add in
        if num not in numbers:
            numbers.append(num)
    numbers.sort()
    #show all nums
    print(" ".join("{:2d}".format(num) for num in numbers))

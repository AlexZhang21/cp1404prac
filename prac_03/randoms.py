"""

What did you see on line 1?
On line 1,I have seen a random integer between 5 and 20, inclusive.

What was the smallest number you could have seen, what was the largest?
The smallest number is 5, the largest number is 20.

What did you see on line 2?
On line 2, I can see a random odd integer between 3 and 9, inclusive.

What was the smallest number you could have seen, what was the largest?
The smallest number is 3, and the largest number is 9.

Could line 2 have produced a 4?
No, line 2 could not have produced a 4, because the step size is 2, and 4 is not an odd number.

What did you see on line 3?
On line 3, I can see a random float between 2.5 and 5.5, inclusive.

What was the smallest number you could have seen, what was the largest?
The smallest number is 2.5, and the largest number is 5.5.

Write code, not a comment, to produce a random number between 1 and 100 inclusive.
"""

import random

random_number = random.randint(1, 100)
print(random_number)

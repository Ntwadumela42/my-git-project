#Quick function to determine if a number is a perfect square.

import math
n = int(input("Please enter a number: "))
def is_square(n):
    if n <= 0:
        return False
    elif math.sqrt(n) == round(math.sqrt(n)):
        return True
    else:
        return False
print(is_square(n))

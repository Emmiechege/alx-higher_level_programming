#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("Last digit of" + str(number) + "is" + str(number[""]))
if number[""] > 5:
    print("and is greater than 5")

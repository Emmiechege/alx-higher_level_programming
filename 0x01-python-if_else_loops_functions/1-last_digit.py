#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    last_digit = number % 10
else:
    last_digit = ((-number % 10) * -1)
# check if num is non negative,if so check last digit using modulo
# if negative,take the absolute value,find last digit and negate it
message = f"Last digit of {number} is {last_digit}"
# formatted sring with original no and its last digit
if last_digit == 0:
    print(f"{message} and is 0")
elif last_digit > 5:
    print(f"{message} and is greater than 5")
else:
    print(f"{message} and is less than 6 and not 0")
# Check the value of 'last_digit' and print a message based on its value:
# - If it's 0, print a message indicating it's 0.
# - If it's greater than 5, print a message indicating it's greater than 5.
# - Otherwise, print a message indicating it's less than 6 and not 0.

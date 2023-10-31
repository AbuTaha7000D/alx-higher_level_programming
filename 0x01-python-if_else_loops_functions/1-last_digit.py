#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
number2 = number % 10
if number >= 0:
    if number2 > 5:
        print("Last digit of", number, "is", number2, "is greater than 5")
    elif number2 == 0:
        print("Last digit of", number, "is", number2, "is 0")
    else:
        print("Last digit of", number, "is", number2, "is less than 6 and not 0")
if number < 0:
    if number2 == 0:
        print("Last digit of", number, "is", number2, "is 0")
    else:
        print("Last digit of", number, "is", number2 - 10, "is less than 6 and not 0")

#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

lastD = 0

if number > 0:
    lastD = number % 10
else:
    number = -number
    lastD = number % 10
    number = -number
    lastD = -lastD

if lastD > 5:
    print(f"Last digit of {number} is {lastD} and is greater than 5")

elif lastD == 0:
    print(f"Last digit of {number} is {lastD} and is 0")

else:
    print(f"Last digit of {number} is {lastD} and is less than 6 and not 0")

"""Write a Python program to demonstrate the use of functions from
the math module. 24) Write a Python program to generate random numbers between 1 and
100 using the random module."""

import math

number = 9.7

print(f"Square root of {number} is {math.sqrt(number)}")

print(f"Ceiling of {number} is {math.ceil(number)}")

print(f"Floor of {number} is {math.floor(number)}")
fact_num = 5

print(f"Factorial of {fact_num} is {math.factorial(fact_num)}")
print(f"{fact_num} raised to the power 3 is {math.pow(fact_num, 3)}")




print()
print("next Program ==>")
print()

import random

random_number = random.randint(1, 100)

print(f"Random number between 1 and 100: {random_number}")

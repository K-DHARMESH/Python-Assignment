# Write a Python program to import the math module and use functions like sqrt(), ceil(), floor().

import math

num = 16.7

sqrt_value = math.sqrt(num)


ceil_value = math.ceil(num)

floor_value = math.floor(num)

print(f"Number: {num}")
print(f"Square root of {num}: {sqrt_value}")
print(f"Ceiling of {num}: {ceil_value}")
print(f"Floor of {num}: {floor_value}")





print()
print("next Program ==>")
print()

# ======= Write a Python program to generate random numbers using the random module.


import random


rand_int = random.randint(1, 10)

rand_float = random.random()

rand_uniform = random.uniform(5, 10)

choices = ['apple', 'banana', 'cherry', 'date']

rand_choice = random.choice(choices)

print("Random integer between 1 and 10:", rand_int)
print("Random float between 0 and 1:", rand_float)
print("Random float between 5 and 10:", rand_uniform)
print("Random choice from list:", rand_choice)

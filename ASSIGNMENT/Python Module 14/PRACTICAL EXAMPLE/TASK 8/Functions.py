""" Write a Python program to print a string using a function. 20) Write
a Python program to create a parameterized function that takes two arguments and prints their
sum. 21) Write a Python program to create a lambda function with one expression. 22) Write
a Python program to create a lambda function with two expressions.
"""


def print_string():
    print("Hello, this is a printed string!")

print_string()


print()
print("next Program ==>")
print()


def print_sum(a, b):
    print(f"The sum of {a} and {b} is {a + b}")

print_sum(5, 7)


print()
print("next Program ==>")
print()


square = lambda x: x * x

print("Square of 6 is", square(6))



print()
print("next Program ==>")
print()

sum_and_product = lambda x, y: (x + y, x * y)

result = sum_and_product(4, 5)
print("Sum:", result[0])
print("Product:", result[1])

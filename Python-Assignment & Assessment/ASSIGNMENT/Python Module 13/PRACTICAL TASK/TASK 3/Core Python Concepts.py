#=============== Write a Python program to demonstrate the creation of variables and different data types.=====================

# Practical Example 1: Python Code Structure:

# Python code is executed line by line from top to bottom
#Comments start with # and are ignored by the interpreter

print("Hello, World!") # This is a simple print statement
print("Python executes code sequentially.")
print()                  # for space



print()
print("Next Program !........")
print()


#=========== Practical Example 2: Creating Variables in Python ============

#Variables are created by assigning a value to a name
# Python is dynamically typed - no need to declare variable types

# 1. Integer variable

age = 20
print("Age:", age)

# 2. Floating point variable

price = 19.99
print("Price:", price)

# 3. String variable

name = "Dharmesh"
print("Name:", name)

# 4. Boolean variable

is_student = True
print("Is student:", is_student)

# 5. List (mutable)

fruits = ["apple", "banana", "cherry"]
print("Fruits:", fruits)

# 6. Tuple (immutable)

coordinates = (10.0, 20.0)
print("Coordinates:", coordinates)

# 7. Dictionary

person = {"name": "Dharmesh", "age": 20}
print("Person:", person)
print()



print()
print("Next Program !........")
print()


# =================================== Practical Example 3: Taking User Input ============================

# The input() function always returns a string:

user_name = input("Enter your name: ")
user_age = input("Enter your age: ")
user_height = input("Enter your height in meters: ")

print("Hello", user_name, "You are",user_age, "years old" "and",user_height, "m tall.")




print()
print("Next Program !........")
print()


# ==================================== Practical Example 4: Checking Variable Types ==============================

# Using type() function to check variable types dynamically:

print("Type of age:", type(age))
print("Type of price:", type(price))
print("Type of name:", type(name))
print("Type of is_student:", type(is_student))
print("Type of fruits:", type(fruits))
print("Type of coordinates:", type(coordinates))
print("Type of person:", type(person))


# Converting types
# user_age_int = int(user_age)
# user_height_float = float(user_height)
# print("After conversion:")
# print("Type of user_age_int:", type(user_age_int))
# print("Type of user_height_float:", type(user_height_float))
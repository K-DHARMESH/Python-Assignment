# === Practical Example 1: Write a Python program to print each fruit in a list using a simple for=======

List1 = ['apple', 'banana', 'mango']
for fruit in List1:
    print(fruit)


print()
print("Next Program !........")
print()


# ============== Practical Example 2: Write a Python program to find the length of each string in List1. =============

List1 = ['apple', 'banana', 'mango']
for fruit in List1:
    print(fruit, len(fruit),"characters")


print()
print("Next Program !........")
print()


# == Practical Example 3: Write a Python program to find a specific string in the list using a simple for loop and if condition ==

List1 = ['apple', 'banana', 'mango']
search_fruit = 'banana'
for fruit in List1:
    if fruit == search_fruit:
        print(search_fruit,"Found in the list!")
        break
else:
    print(search_fruit,"not found in the list")



print()
print("Next Program !........")
print()

# Practical Example 4: Print this pattern using nested for loop:
# markdown
# Copy code

# *
# **
# ***
# ****
# *****

# first way:

for i in range(1, 6):
    print("*" * i)

# second way:

for i in range(1, 6):
    for j in range(1, i+1):
        print("*", end= "")
    print()
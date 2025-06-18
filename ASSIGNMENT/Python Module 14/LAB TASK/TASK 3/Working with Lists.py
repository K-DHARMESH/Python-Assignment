# ====== Write a Python program to iterate over a list using a for loop.


colors = ['red', 'green', 'blue', 'yellow', 'purple']

print("List of colors:")

for color in colors:
    print(color)




print()
print("next Program ==>")
print()


# ==== Write a Python program to sort a list using both sort() and sorted().

numbers = [42, 17, 23, 100, 8, 56]

print("Original list:", numbers)


sorted_numbers = sorted(numbers)
print("sorted():", sorted_numbers)

print("original", numbers)  

numbers.sort()
print(" sort():", numbers)  

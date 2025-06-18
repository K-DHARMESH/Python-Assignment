# =========== Write a Python program to create a list with elements of multiple data types (integers,strings, floats, etc.).===


mixed_list = [42, "Hello, world!", 3.14, True, (4, 5)]


print(mixed_list)

print("\nMixed data type list:")

for elements in mixed_list:
    print(type(elements))



print()
print("next Program ==>")
print()


# ========= Write a Python program to access elements at different index positions. ====================

my_list = ['apple', 10, 3.14, True, 'banana']

print("o inadex",my_list[0])
print("3 inadex",my_list[3])
print("-1 inadex",my_list[-1])
print("2 inadex",my_list[2])

print("\nAccess all index of elements :")

for i in range(len(my_list)):
    print(f"Index of elements {i} : {my_list[i]}")



print()
print("next Program ==>")
print()



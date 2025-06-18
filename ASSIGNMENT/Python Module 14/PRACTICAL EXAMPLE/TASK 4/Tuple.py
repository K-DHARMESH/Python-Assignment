""" Write a Python program to convert a list into a tuple. 8) Write a
Python program to create a tuple with multiple data types. 9) Write a Python program to
concatenate two tuples into one. 10) Write a Python program to access the value of the first
index in a tuple.
"""



my_list = [10, 20, 30, 40]


my_tuple = tuple(my_list)


print("Original list:", my_list)
print("Converted tuple:", my_tuple)





print()
print("next Program ==>")
print()


mixed_tuple = (42, 3.14, "Python", False, [1, 2, 3])

print("Tuple with multiple data types:")
print(mixed_tuple)



print()
print("next Program ==>")
print()


tuple1 = ('apple', 'banana')
tuple2 = ('cherry', 'date')


combined_tuple = tuple1 + tuple2

print("Concatenated tuple:", combined_tuple)



print()
print("next Program ==>")
print()



sample_tuple = ('red', 'green', 'blue')

first_element = sample_tuple[0]

print("First element in the tuple:", first_element)

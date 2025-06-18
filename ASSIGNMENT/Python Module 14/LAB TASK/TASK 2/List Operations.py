# =============== Write a Python program to add elements to a list using insert() and append().

my_list = []

my_list.append(10)
my_list.append("ok")
my_list.append("hello")

print(f"append mode : {my_list}")

my_list.insert(1,"good")
my_list.insert(2,"mornig")


print(f"insert mode : {my_list}")



print()
print("next Program ==>")
print()
# ============================== Write a Python program to remove elements from a list using pop() and remove()


fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']

print("Original list:", fruits)

fruits.pop(2)
print("after pop :", fruits)

fruits.remove('banana')
print("remove('banana'):", fruits)

# ============= Write a Python program to update a value in a dictionary


employee = {
    "name": "Dharmesh",
    "position": "Developer",
    "salary": 500000
}


print("Original Dictionary:")
print(employee)

employee["salary"] = 600000

print("Updated Dictionary :")
print(employee)



print()
print("next Program ==>")
print()


# Write a Python program to merge two lists into one dictionary using a loop.


keys = ['name', 'age', 'city']
values = ['Alice', 30, 'New York']


merged_dict = {}

for i in range(len(keys)):
    merged_dict[keys[i]] = values[i]


print("Merged Dictionary:")
print(merged_dict)

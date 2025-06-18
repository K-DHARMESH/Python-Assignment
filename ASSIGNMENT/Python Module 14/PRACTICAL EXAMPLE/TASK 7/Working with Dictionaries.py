"""Write a Python program to update a value at a particular key in a
dictionary. 16) Write a Python program to separate keys and values from a dictionary using
keys() and values() methods. 17) Write a Python program to convert two lists into one
dictionary using a for loop. 18) Write a Python program to count how many times each
character appears in a string"""



student = {
    "name": "Dharmesh",
    "grade": "A",
    "age": 20
}

student["grade"] = "A+"

print("Updated Dictionary:")
print(student)


print()
print("next Program ==>")
print()



info = {
    "brand": "Nike",
    "type": "Shoes",
    "price": 120
}


keys = list(info.keys())
values = list(info.values())

print("Keys:", keys)
print("Values:", values)


print()
print("next Program ==>")
print()




keys = ['id', 'name', 'score']
values = [101, 'Alice', 95]


combined_dict = {}

for i in range(len(keys)):
    combined_dict[keys[i]] = values[i]

print("Combined Dictionary:")
print(combined_dict)




print()
print("next Program ==>")
print()



text = "hello world"
char_count = {}


for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print("Character Frequency:")
for char, count in char_count.items():
    print(f"'{char}': {count}")

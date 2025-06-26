"""Write a Python program to search for a word in a string using
re.search(). 24) Write a Python program to match a word in a string using re.match()."""


import re

text = "Welcome to Python programming."
word = "Python"

match = re.search(word, text)

if match:
    print(f"'{word}' found in the string.")
else:
    print(f"'{word}' NOT found in the string.")


print()
print("next ...")
print()


import re

text = "Python is awesome."
word = "Python"

match = re.match(word, text)

if match:
    print(f"The string starts with '{word}'.")
else:
    print(f"The string does NOT start with '{word}'.")

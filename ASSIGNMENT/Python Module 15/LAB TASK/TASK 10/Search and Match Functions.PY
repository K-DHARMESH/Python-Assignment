"""Write a Python program to search for a word in a string using re.search()."""

import re

text = "Hello, welcome to the world of Python programming."

word = "Python"

match = re.search(word, text)

if match:
    print(f"The word '{word}' was found in the text.")
else:
    print(f"The word '{word}' was NOT found in the text.")


print()
print("next ..")
print()

"""Write a Python program to match a word in a string using re.match()."""



import re

text = "Python is a powerful language."


word = "Python"

match = re.match(word, text)

if match:
    print(f"The string starts with the word '{word}'.")
else:
    print(f"The string does NOT start with the word '{word}'.")


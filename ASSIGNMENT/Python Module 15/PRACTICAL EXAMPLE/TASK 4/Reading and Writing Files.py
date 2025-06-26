"""Write a Python program to create a file and print the string into the
file. 5) Write a Python program to read a file and print the data on the console. 6) Write a
Python program to check the current position of the file cursor using tell()."""


filename = "my_file.txt"

text = "This string will be written to the file."

with open(filename, "w") as file:
    file.write(text)

print(f"The text has been written to '{filename}'.")


print()
print()



filename = "my_file.txt"

try:
    with open(filename, "r") as file:
        data = file.read()
    
    print("File contents:")
    print(data)

except FileNotFoundError:
    print(f"The file '{filename}' does not exist.")



print()
print()



filename = "my_file.txt"

try:
    with open(filename, "r") as file:

        file.read(10)
        
        position = file.tell()

        print(f"Current file cursor position: {position}")

except FileNotFoundError:
    print(f"The file '{filename}' does not exist.")

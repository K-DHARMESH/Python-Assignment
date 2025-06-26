"""Write a Python program to read the contents of a file and print them on the console."""

filename = "output.txt"

try:

    with open(filename, "r") as file:
        contents = file.read()

    print("File contents:")
    print(contents)

except FileNotFoundError:
    print(f"The file '{filename}' does not exist.")



print("\nnext program.....")
print()

"""Write a Python program to write multiple strings into a file."""



filename = "multiline_output.txt"

lines = [
    "First line of text.",
    "Second line of text.",
    "Third line of text."
]

with open(filename, "w") as file:
    for line in lines:
        file.write(line + "\n")  

print(f"{len(lines)} lines have been written to '{filename}'.")



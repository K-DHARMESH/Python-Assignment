"""Write a Python program to handle exceptions in a calculator. 8)
Write a Python program to handle multiple exceptions (e.g., file not found, division by zero).
9) Write a Python program to handle file exceptions and use the finally block for closing
the file. 10) Write a Python program to print custom exceptions.
"""


try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operator = input("Enter operator (+, -, *, /): ")

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero!")
        result = num1 / num2
    else:
        raise ValueError("Invalid operator!")

    print(f"Result: {result}")

except ZeroDivisionError as zde:
    print(f"Error: {zde}")

except ValueError as ve:
    print(f"Error: {ve}")

except Exception as e:
    print(f"Unexpected error: {e}")



print()
print("next program ....")
print()


try:
    filename = input("Enter filename to read: ")
    with open(filename, 'r') as file:
        data = file.read()
        print("File content:")
        print(data)
    
    x = int(input("Enter a number to divide 10 by: "))
    result = 10 / x
    print(f"Result: {result}")

except FileNotFoundError:
    print("Error: File not found!")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed!")

except ValueError:
    print("Error: Invalid input!")

except Exception as e:
    print(f"Unexpected error: {e}")



print()
print("next program....")
print()

filename = "example.txt"

try:
    file = open(filename, "r")
    content = file.read()
    print("File contents:")
    print(content)

except FileNotFoundError:
    print("Error: The file does not exist!")

finally:
    try:
        file.close()
        print("File closed successfully.")
    except NameError:
        
        print("File was never opened, so no need to close.")


print()
print("next program ....")
print()

class NegativeNumberError(Exception):
    def __init__(self, message="Negative numbers are not allowed"):
        self.message = message
        super().__init__(self.message)

try:
    num = int(input("Enter a positive number: "))
    if num < 0:
        raise NegativeNumberError()
    print(f"You entered: {num}")

except NegativeNumberError as nne:
    print(f"Custom Exception: {nne}")

except ValueError:
    print("Error: Please enter a valid integer.")

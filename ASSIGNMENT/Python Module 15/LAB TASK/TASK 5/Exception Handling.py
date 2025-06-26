"""Write a Python program to handle exceptions in a simple calculator (division by zero, invalid
input)."""


try:

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Enter an operator (+, -, *, /): ")


    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
    
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        result = num1 / num2
    else:
        raise ValueError("Invalid operator.")

    print(f"Result: {result}")

except ValueError as ve:
    print("ValueError:", ve)

except ZeroDivisionError as zde:
    print("ZeroDivisionError:", zde)

except Exception as e:
    print("An unexpected error occurred:", e)


print()
print()

""""Write a Python program to demonstrate handling multiple exceptions."""


try:

    num1 = int(input("Enter the first integer: "))
    num2 = int(input("Enter the second integer: "))
    
    result = num1 / num2
    
    print(f"Result of {num1} / {num2} = {result}")

except ZeroDivisionError:
    print("Error: You can't divide by zero!")

except ValueError:
    print("Error: Invalid input. Please enter an integer.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")

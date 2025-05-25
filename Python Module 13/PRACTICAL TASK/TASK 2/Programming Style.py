
# =========================Demonstrates PEP 8 guidelines including indentation, comments, and variable naming==========================


def add_two_numbers(a, b): 
    """Return the sum of two numbers."""           # comments
    result = a + b  # Add the numbers              # indentation
    return result


num1 = 5                                            # variable naming
num2 = 3
sum_result = add_two_numbers(num1, num2)
print("Sum:", sum_result)


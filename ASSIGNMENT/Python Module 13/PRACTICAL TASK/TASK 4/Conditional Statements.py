# ===================== Practical Example 5: Write a Python program to find greater and less than a number using if_else.=========


n1 = int(input(" enter the numbern1  :"))

n2 = int(input("enter the number n2  :"))

n3 = int(input("enter the number n3  :"))

if n1>n2:
    if n1>n3:
        print(n1, " n1 is grater than n2..")
    else:
       print(n3, " n3 is grater than n1..")
else:
    if n2>n3:
        print(n2, " n2 is grater than n3")
    else:
        print(n3, " n3 is grater than n2")




print()
print("Next Program !........")
print()

# ====================== Practical Example 6: Write a Python program to check if a number is prime using if_else. ==============


num = int(input("Enter a number to check if prime: "))

if num <= 1:
    print(f"{num} is not a prime number")
elif num == 2:
    print(f"{num} is a prime number")
elif num % 2 == 0:
    print(f"{num} is not a prime number (divisible by 2)")
elif num == 3:
    print(f"{num} is a prime number")
elif num % 3 == 0:
    print(f"{num} is not a prime number (divisible by 3)")
elif num == 5:
    print(f"{num} is a prime number")
elif num % 5 == 0:
    print(f"{num} is not a prime number (divisible by 5)")
elif num == 7:
    print(f"{num} is a prime number")
elif num % 7 == 0:
    print(f"{num} is not a prime number (divisible by 7)")
else:
    # This isn't perfect for numbers > 121 (7*7)
    print(f"{num} is a prime number")



print()
print("Next Program !........")
print()


# =============== Practical Example 7: Write a Python program to calculate grades based on percentage using if-else ladder =======

percentage = float(input("Enter your percentage: "))

if percentage >= 90:
    grade = 'A'
elif percentage >= 80:
    grade = 'B'
elif percentage >= 70:
    grade = 'C'
elif percentage >= 60:
    grade = 'D'
elif percentage >= 40:
    grade = 'E'
else:
    grade = 'F'

print("Your grade is :", grade)
print()





print()
print("Next Program !........")
print()

# =====  Practical Example 8: Write a Python program to check if a person is eligible to donate blood using a nested if. =====

age = int(input("Enter your age: "))
weight = float(input("Enter your weight in kg: "))
health_status = input("Are you healthy? (yes/no): ")  # for lower number Enter

if age >= 18:
    if weight >= 50:
        if health_status == 'yes':
            print("You are eligible to donate blood!")
        else:
            print("You are not eligible due to health issues")
    else:
        print("You are not eligible (weight should be 50kg or more)")
else:
    print("You are not eligible (minimum age is 18)")
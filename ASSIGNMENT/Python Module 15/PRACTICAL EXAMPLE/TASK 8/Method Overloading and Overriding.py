"""Write a Python program to show method overloading. 20) Write a
Python program to show method overriding."""

class Calculator:

    def add(self, a, b, c=0):
        return a + b + c


    def add_multiple(self, *numbers):
        return sum(numbers)

calc = Calculator()

print(calc.add(5, 10))         
print(calc.add(5, 10, 15))     
print(calc.add_multiple(1, 2, 3, 4, 5))  


print()
print("next ..")
print()



class Vehicle:
    def move(self):
        print("Vehicle is moving")

class Car(Vehicle):

    def move(self):
        print("Car is driving")


v = Vehicle()
v.move()  

c = Car()
c.move()  

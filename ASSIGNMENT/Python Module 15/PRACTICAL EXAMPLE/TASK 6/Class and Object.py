"""Write a Python program to create a class and access the properties
of the class using an object. 12) Write a Python program to demonstrate the use of local and
global variables in a class.
"""

class Car:
    def __init__(self, brand, model):
        self.brand = brand  
        self.model = model  

my_car = Car("Toyota", "Corolla")

print(f"Brand: {my_car.brand}")
print(f"Model: {my_car.model}")



print()
print()



manufacturer = "Global Motors"

class Bike:
    def __init__(self, model):
        self.model = model  

    def show_info(self):
    
        year = 2023
        print(f"Manufacturer: {manufacturer}")  
        print(f"Model: {self.model}")            
        print(f"Year: {year}")                    

bike1 = Bike("Harley")
bike1.show_info()

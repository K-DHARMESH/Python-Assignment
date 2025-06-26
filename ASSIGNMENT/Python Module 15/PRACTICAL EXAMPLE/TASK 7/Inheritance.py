"""Write a Python program to show single inheritance. 14) Write a
Python program to show multilevel inheritance. 15) Write a Python program to show multiple
inheritance. 16) Write a Python program to show hierarchical inheritance. 17) Write a Python
program to show hybrid inheritance. 18) Write a Python program to demonstrate the use of
super() in inheritance."""


class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet_child(self):
        print("Hello from Child")

child = Child()
child.greet()        
child.greet_child()  


print()
print("next ...")
print()


class Grandparent:
    def grandparent_method(self):
        print("Grandparent method")

class Parent(Grandparent):
    def parent_method(self):
        print("Parent method")

class Child(Parent):
    def child_method(self):
        print("Child method")


c = Child()
c.grandparent_method()
c.parent_method()
c.child_method()

print()
print("next ...")
print()

class Father:
    def skills_father(self):
        print("Father's skills")

class Mother:
    def skills_mother(self):
        print("Mother's skills")

class Child(Father, Mother):
    def skills_child(self):
        print("Child's skills")


child = Child()
child.skills_father()
child.skills_mother()
child.skills_child()


print()
print("next ...")
print()

class Parent:
    def parent_method(self):
        print("Parent method")

class Child1(Parent):
    def child1_method(self):
        print("Child1 method")

class Child2(Parent):
    def child2_method(self):
        print("Child2 method")

c1 = Child1()
c2 = Child2()

c1.parent_method()
c1.child1_method()

c2.parent_method()
c2.child2_method()



print()
print("next ...")
print()



class A:
    def method_a(self):
        print("Method A")

class B(A):
    def method_b(self):
        print("Method B")

class C(A):
    def method_c(self):
        print("Method C")

class D(B, C):
    def method_d(self):
        print("Method D")


obj = D()
obj.method_a()
obj.method_b()
obj.method_c()
obj.method_d()



print()
print("next ...")
print()


class Parent:
    def __init__(self):
        print("Parent constructor called")

    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def __init__(self):
        super().__init__()  
        print("Child constructor called")

    def greet(self):
        super().greet()  
        print("Hello from Child")

child = Child()
child.greet()

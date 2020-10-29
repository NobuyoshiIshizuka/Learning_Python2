"""
Python Classes/Objects
Python is an object oriented programming language.

Almost everything in Python is an object, with its properties and methods.

A Class is like an object constructor, or a "blueprint" for creating objects
"""

#Create a class named MyClass, with a property named x
class MyClass:
    x = 5

print(MyClass)

"""
Create Object
Now we can use the class named MyClass to create objects:
"""

#Create an object named p1, and print the value of x:
primary_object = MyClass()
print(primary_object.x)

"""
All classes have a function called __init__(), which is always executed when the class is being initiated.

Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:
"""

#Create a class named Person, use the __init__() function to assign values for name and age:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person_one = Person("John", 26)

print("Name: ", person_one.name)
print("age: ", person_one.age)

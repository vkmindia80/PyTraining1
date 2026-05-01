# Python Classes/Objects
'''Python is an object oriented programming language.
Almost everything in Python is an object, with its properties and methods.
A Class is like an object constructor, or a "blueprint" for creating objects.
Create a Class
To create a class, use the keyword class:
Example
Create a class named MyClass, with a property named x:

class MyClass:
    x = 5
print(MyClass)
# output: <class '__main__.MyClass'>

Create Object
Now we can use the class named MyClass to create objects:
Example
Create an object named obj1, and print the value of x:
class MyClass:
    x = 5
obj1= MyClass()
print(obj1.x)

The __init__() Function
All classes have a function called __init__(), which is always executed when the
class is being initiated. Generally we call it constructor function.
Use the __init__() function to assign values to object properties, or other
operations that are necessary to do when the object is being created: Ex: setting
default values to object properties.
Example
Create a class named Person, use the __init__() function to assign values for name
and age:

class Person:
    def __init__(self, name, age, phone):
        self.name = name
        self.age = age
        self.phone = phone
p1 = Person("John", 36, 3139131569)
p2 = Person("Hugo", 23, 313)
print(p1.name, p1.age, p1.phone)
print(p2.name, p2.age)

Note: The __init__() function is called automatically every time the class is being
used to create a new object.
The __str__() Function
The __str__() function controls what should be returned when the class object is
represented as a string.
If the __str__() function is not set, the string representation of the object is
returned:
Example
The string representation of an object WITHOUT the __str__() function:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("John", 36)
print(p1) # printing object directly gives object info as show below. Output: <__main__.Person object at 0x000002463E1970E0>
print(p1.name, p1.age)

Example
The string representation of an object with the __str__() function:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name},({self.age})"
p1 = Person("John", 36)
print(p1) # printing object directly gives object data as show below

Object Methods
Objects can also contain methods. Methods in objects are functions that belong to
the object.
Let us create a method in the Person class:
Example
Insert a function that prints a greeting, and execute it on the p1 object:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("Hello my name is " + self.name)
p1 = Person("John", 36)
p1.myfunc()

The self ParameterThe self parameter is a reference to the current instance of the class, and is used
to access variables that belong to the class.
It does not have to be named self, you can call it whatever you like, but it has to
be the first parameter of any function in the class:
Example
Use the words mysillyobject and abc instead of self:

class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age
    def myfunc(abc):
        print("Hello my name is " + abc.name, abc.age)
p1 = Person("John", 36)
p1.myfunc()
# Modify Object Properties
# You can modify properties on objects like this:
# Example
# Set the age of p1 to 40:
p1.age = 40
p1.myfunc()
# Delete Object Properties
# You can delete properties on objects by using the del keyword:
# Example
# Delete the age property from the p1 object:
# del p1.age
# p1.myfunc()
# output: AttributeError: 'Person' object has no attribute 'age'

# Delete ObjectsYou can delete objects by using the del keyword:
# Example
# Delete the p1 object:
del p1
p1.myfunc()
# Output: NameError: name 'p1' is not defined

The pass Statement
class definitions cannot be empty, but if you for some reason have
a class definition with no content, put in the pass statement to avoid getting an
error.
Example

class Person:
    pass

Class Attribute
Class attributes are those variables that belong to a class and whose value is shared
among all the instances of that class. A class attribute remains the same for every
instance of the class. a class attribute is available to the class as well as its object.
The object name followed by dot notation (.) is used to access class attributes.
Example

class Employee:
# class attribute
    empCount = 0
    def __init__(self, name, age):
        self.__name = name #instace variable
        self.__age = age #instace variable
        # modifying class attribute
        Employee.empCount += 1
        print ("Name:", self.__name, ", Age: ", self.__age)
        # accessing class attribute
        print ("Employee Count:", Employee.empCount)
e1 = Employee("Ravi", 24)
print()
e2 = Employee("Rajesh", 26)
print()

Class method
What is a class method?
A class method is a method that is bound to a class rather than its object. It doesn't
require creation of a class instance, much like static method.
The difference between a static method and a class method is:
 Static method knows nothing about the class and just deals with the
parameters
 Class method works with the class since its parameter is always the class
itself.
The class method can be called both by the class and its object.
Syntax : Class.classmethod()
def classMethod(cls, args...)
class method is always attached to a class with the first argument as the class itself
cls.
Example1
Example 1: Create class method using classmethod()

class Person:
    age = 25
    def printAge(cls):
        print('The age is:', cls.age)
# create showAge class method
Person.showAge = classmethod(Person.printAge)
Person.showAge()

class Person:
    name = "Vijay"
    def printName(cls):
        print('My name is:', cls.name)
# create showAge class method
Person.showName = classmethod(Person.printName)
Person.showName()
print(Person.name)
# Person.name is protected variable

Example2
'''
class Student:
    marks = 0
    def compute_marks(cls, obtained_marks):
        cls.marks = obtained_marks
        print('Obtained Marks:', cls.marks)
# convert compute_marks() to class method
Student.print_marks = classmethod(Student.compute_marks)
Student.print_marks(38)

More Examples
Access Class Attributes Using Objects
class Parrot:
# class attribute
name = ""
age = 0
# create parrot1 object
parrot1 = Parrot()
parrot1.name = "Blu"
parrot1.age = 10
# create another object parrot2
parrot2 = Parrot()
parrot2.name = "Woo"
parrot2.age = 15
# access attributes
print(f"{parrot1.name} is {parrot1.age} years old")
print(f"{parrot2.name} is {parrot2.age} years old")
Output:
Blu is 10 years old
Woo is 15 years old
Example 2:
# define a classclass Bike:
name = ""
gear = 0
# create object of class
bike1 = Bike()
# access attributes and assign new values
bike1.gear = 11
bike1.name = "Mountain Bike"
print(f"Name: {bike1.name}, Gears: {bike1.gear} ")
Output:
Name: Mountain Bike, Gears: 11
Create Multiple Objects of Python Class
We can also create multiple objects from a single class. For example,
# define a class
class Employee:
# define a property
employee_id = 0
# create two objects of the Employee class
employee1 = Employee()
employee2 = Employee()
# access property using employee1
employee1.employeeID = 1001
print(f"Employee ID: {employee1.employeeID}")
# access properties using employee2
employee2.employeeID = 1002
print(f"Employee ID: {employee2.employeeID}")
Output:
Employee ID: 1001
Employee ID: 1002
Using Python Methods
# create a class
class Room:
length = 0.0
breadth = 0.0
# method to calculate area
def calculate_area(self):
print("Area of Room =", self.length * self.breadth)
# create object of Room classstudy_room = Room()
# assign values to all the properties
study_room.length = 42.5
study_room.breadth = 30.8
# access method inside class
study_room.calculate_area()
Output
Area of Room = 1309.0
Python Constructors
class Bike:
# constructor function
def __init__(self, name = ""):
self.name = name
print("Bike Name =", self.name)
bike1 = Bike()
bike1 = Bike("Scoty")
Output
Bike Name = Scoty


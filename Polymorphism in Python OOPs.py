# Polymorphism in Python OOPs
The word "polymorphism" means "many forms", and in programming it refers to
methods/functions/operators with the same name that can be executed on many
objects or classes.
Function Polymorphism
There are some functions in Python which are compatible to run with multiple data
types.
One such function is the len() function. It can run with many data types in Python.
Let's look at some example use cases of the function.
Example
print(len("Hello World"))
print(len(["Python", "Java", "C"]))
print(len({"Name": "John", "Address": "Nepal"}))

Class Polymorphism
Polymorphism is often used in Class methods, where we can have multiple classes
with the same method name.
For example, say we have three classes: Car, Boat, and Plane, and they all have a
method called move():

Example
Different classes with the same method:
class Car:
def __init__(self, brand, model):
self.brand = brand
self.model = model
def move(self):
print("Drive!")
class Boat:
def __init__(self, brand, model):
self.brand = brandself.model = model
def move(self):
print("Sail!")
class Plane:
def __init__(self, brand, model):
self.brand = brand
self.model = model
def move(self):
print("Fly!")
car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object
for x in (car1, boat1, plane1):
x.move()

o/p:
Drive!
Sail!
Fly!
Look at the for loop at the end. Because of polymorphism we can execute the
same method for all three classes.
Polymorphism in Inheritance
What about classes with child classes with the same name? Can we use
polymorphism there?
Yes. If we use the example above and make a parent class called Vehicle,
and make Car, Boat, Plane child classes of Vehicle, the child classes inherits
the Vehicle methods, but can override them:

Example
Create a class called Vehicle and make Car, Boat, Plane child classes
of Vehicle:
class Vehicle:
def __init__(self, brand, model):
self.brand = brand
self.model = model
def move(self):
print("Move!")
class Car(Vehicle):
pass
class Boat(Vehicle):
def move(self):
print("Sail!")
class Plane(Vehicle):def move(self):
print("Fly!")
car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object
for x in (car1, boat1, plane1):
print(x.brand)
print(x.model)
x.move()
o/p:
Ford
Mustang
Move!
Ibiza
Touring 20
Sail!
Boeing
747
Fly!
Child classes inherits the properties and methods from the parent class.
In the example above you can see that the Car class is empty, but it
inherits brand, model, and move() from Vehicle.
The Boat and Plane classes also inherit brand, model, and move() from Vehicle, but
they both override the move() method.
Because of polymorphism we can execute the same method for all classes.
More Example to Practice
Oops feature polymorphism implemented in different ways in Python
1. Method overloading – occurs in functions, classes(class polymorphism).
2. Method overriding – occurs in inheritance.1. Method Overloading in a class
class example:
def add(self, a, b):
x = a+b
return x
def add(self, a, b, c):
x = a+b+c
return x
obj = example()
print (obj.add(10,20,30))
print (obj.add(10,20))
60
Traceback (most recent call last):
File "C:\Users\user\example.py", line 12, in <module>
print (obj.add(10,20))
^^^^^^^^^^^^^^
TypeError: example.add() missing 1 required positional argument: 'c
class example:
def add(self, a = None, b = None, c = None):
x=0
if a !=None and b != None and c != None:
x = a+b+c
elif a !=None and b != None and c == None:
x = a+b
return x
obj = example()
print (obj.add(10,20,30))
print (obj.add(10,20))
# o/p
60
30
Or
def add(*nums):
return sum(nums)
# Call the function with different number of parameters
result1 = add(10,20)
result2 = add(10,20,30)
print(result1)
print(result2)
Example2:1. Method Overriding in multiple classes
class Cat:
def __init__(self, name, age):
self.name = name
self.age = age
def info(self):
print(f"I am a cat. My name is {self.name}. I am {self.age} years
old.")
def make_sound(self):
print("Meow")
class Dog:
def __init__(self, name, age):
self.name = name
self.age = age
def info(self):
print(f"I am a dog. My name is {self.name}. I am {self.age} years
old.")
def make_sound(self):
print("Bark")
cat1 = Cat("Kitty", 2.5)
dog1 = Dog("Fluffy", 4)
for animal in (cat1, dog1):
animal.make_sound()
animal.info()
animal.make_sound()
o/p:
Meow
I am a cat. My name is Kitty. I am 2.5 years old.
Meow
Bark
I am a dog. My name is Fluffy. I am 4 years old.
Bark
2. Method Overriding in inheritance classes
class Polygon:
# method to render a shape
def render(self):
print("Rendering Polygon...")
class Square(Polygon):
# renders Square
def render(self):
print("Rendering Square...")
class Circle(Polygon):
# renders circledef render(self):
print("Rendering Circle...")
# create an object of Square
s1 = Square()
s1.render()
# create an object of Circle
c1 = Circle()
c1.render()
o/p:
Circle
I am a two-dimensional shape.
Squares have each angle equal to 90 degrees.
153.93804002589985
Example 2:
from math import pi
class Shape:
def __init__(self, name):
self.name = name
def area(self):
pass
def fact(self):
return "I am a two-dimensional shape."
def __str__(self):
return self.name
class Square(Shape):
def __init__(self, length):
super().__init__("Square")
self.length = length
def area(self):
return self.length**2
def fact(self):
return "Squares have each angle equal to 90 degrees."
class Circle(Shape):
def __init__(self, radius):
super().__init__("Circle")
self.radius = radius
def area(self):
return pi*self.radius**2
a = Square(4)
b = Circle(7)
print(b)
print(b.fact())print(a.fact())
print(b.area())
o/p
Circle
I am a two-dimensional shape.
Squares have each angle equal to 90 degrees.
153.93804002589985
3. Operator Overloading
It allows adding two objects of same class Ex: obj1 + obj2
class Vector:
def __init__(self, a, b):
self.a = a
self.b = b
def __str__(self):
return 'Vector (%d, %d)' % (self.a, self.b)
def __add__(self,other):
return Vector(self.a + other.a, self.b + other.b)
v1 = Vector(2,10)
v2 = Vector(5,-2)
print (v1 + v2)
o/p:
Vector(7,8)
Dynamic Binding
class shape:
def draw(self):
print ("draw method")
return
class circle(shape):
def draw(self):
print ("Draw a circle")
return
class rectangle(shape):
def draw(self):
print ("Draw a rectangle")
return
shapes = [circle(), rectangle()]
for shp in shapes:
shp.draw()Inner Classes
class student:
def __init__(self):
self.name = "Ashish"
self.subs = self.subjects()
return
def show(self):
print ("Name:", self.name)
self.subs.display()
class subjects:
def __init__(self):
self.sub1 = "Phy"
self.sub2 = "Che"
return
def display(self):
print ("Subjects:",self.sub1, self.sub2)
s1 = student()
s1.show()
o/p:
Name: Ashish
Subjects: Phy Che

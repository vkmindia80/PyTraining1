# Python Input statement: This will accept data from keyboard.
# Example1:
# input.py
'''name = input('Enter your name: ')
age = input('Enter your age: ')
height = input('Enter your height: ')
# Display the details using Output(print) statement
print('Name: '+name)
print('Age: '+age)
print('Height: '+height)

num = input('Enter a number: ')
print('You Entered:', num)
print('Data type of num:', type(num))

a = input('Enter first number: ')
b = input('Enter second number: ')
# Add two numbers
sum = int(a) + int(b) # adds two numbers
# sum = a + b # combine two numbers sidebyside
# Display the sum
print(sum)

It can converted while inputting data
Example 4:
Typecast2.py
a = int(input("Enter first number: " ))
b = int(input("Enter second number: " ))
sum = a + b
print ( "first no = ", a )
print ( "second no=", b )
print ( "sum = ", sum )

# Accept student details
rollno = 100
name = "Vijay Marupudi"
marks1 = 75
marks2 = 73
marks3 = 83
total = (marks1 + marks2 + marks3)
average = total / 3
print ("Total = ", total)
print ("Average = ", average)


# Ex2: Complete the given program
# To take inputs from the user
x = input('Enter value of x: ')
y = input('Enter value of y: ')
print (x, y)
# create a temporary variable and swap the values
temp = x
x = y
y = temp
print (x, y)
'''
import mymodule
mymodule.greeting("Jonathan")
a = mymodule.person1["age"]
print(a)
'''
Example
Import the module named mymodule, and access the person1 dictionary:
import mymodule
a = mymodule.person1["age"]
print(a)
o/p:
36Naming a Module
You can name the module file whatever you like, but it must have the file
extension .py
Re-naming a Module
You can create an alias when you import a module, by using the as keyword:
Example
Create an alias for mymodule called mx:
'''
import mymodule as mx
a = mx.person1["age"]
print(a)

import platform
x = platform.system()
print(x)

import platform
x = dir(platform)
print(x)

from mymodule import person1
print (person1["age"])

# import all names from the standard module math
from math import *
print("The value of pi is", pi)
# import only pi from math module
from math import pi
print(pi)
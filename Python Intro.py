# Check the Python in PC
# Open command prompt and type the following command.
# C:\>python –version
# Syntax to run a file at command line: C:\Users\yourdir>python helloworld.py
# Python comment prefixed with (#)
# This is a comment
# Multiline comments start with (''' and ends with ''')

'''
line one
line two
line N..
'''

print("Hello, World!")

# Using blank lines: \n
print("\nMy name is Vijay Marupudi")

# To open python interpretor, at prompt type: C:\>python or c:\> py
# Then you will see the python prompt(>>>) where you can type python commands as: >>> print ("Hello, World!")
# To quit the python command line interface: exit()

# Python uses indentation to indicate a block of code.
# if 5 > 2:
# print("yes")
#The number of spaces is up to you as a programmer, but it has to be at least one.

if 5 > 2:
 print("Yes!")

print(5)

# A variable is created the moment you first assign a value to it.
x=3
print (x)
y=6
print(y)
print (x+y)
x = 4 # x is of type int
x = "Sally" # x is now of type str
print(x)
a = "Hello World"
b = 100
c = 25.50
d = 5+6j
print ("Message: ", a)
print (b, c, b-c)
print(pow(100, 0.5), pow(c,2))

# A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
#  A variable name must start with a letter or the underscore character
#  A variable name cannot start with a number
#  Contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
#  Variable names are case-sensitive (age, Age and AGE are three different variables)
# myvar = "John"
# my_var = "John"
# my_var = "John"
# myVar = "John"
# MYVAR = "John"
# myvar2 = "John"
# Not Allowed:
# 2myvar = "John"
# my-var = "John"
# my var = "John"

# Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
print(x,y,z)

# One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpack a Collection: If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Output Variables: The Python print() function is often used to output variables.
x = "Python is awesome"
print(x)
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
x = 5
y = 10
print(x + y)
x = 5
y = "John"
# print(x + y) --> Errors out as TypeError: unsupported operand type(s) for +: 'int' and 'str'

# printing multiple variables
x = 5
y = "John"
print(x, y)

# printing multiple variables with specific separator
city="Hyderabad"
state="Telangana"
country="India"
print(city, state, country, sep=',')

# To make these two lines appear in the same line, define end parameter in the first print() function and set it to a whitespace string " "
city="Hyderabad"
state="Telangana"
country="India"
print("City:", city, end=" ")
print("State:", state)

# Global variables can be used by everyone, both inside of functions and outside.
x = "awesome"
def myfunc():
    print("Python is " + x)
myfunc()
x = "awesome"
def myfunc():
    print("Python is " + city)
myfunc()

# If you use the global keyword, the variable belongs to the global scope:
def myfunc():
    global x
x = "fantastic"
myfunc()
print("Python is " + x)

# To change the value of a global variable inside a function, refer to the variable by using the global keyword:
x = "awesome"
def myfunc():
    global x
    x = "fantastic"
myfunc()
print("Python is " + x)

# Python Editors
# PyCharm: https://www.jetbrains.com/pycharm/download
# VSCode: https://code.visualstudio.com/download
#   Install code runner extension.
#   Install Microsoft python language support extension.

# input() method.
# The following example asks for the username, and when you entered the username, it gets printed on the screen:
'''username = input("Enter username:")
print("Username is: " + username)
name = input("Eneter your name - ")
city = input("Enter city name - ")
print ("Hello My name is", name)
print ("I am from ", city)
'''
# numeric input
'''width = input("Enter width : ")
height = input("Enter height : ")
area = width*height
print ("Area of rectangle = ", area)
'''
# string to int
'''width = int(input("Enter width : "))
height = int(input("Enter height : "))
area = width*height
print ("Area of rectangle = ", area)
'''
# string to float (Statements must be separated by newlines or semicolons)
# amount = float(input("Enter Amount : ")) rate = float(input("Enter rate of interest : "))
'''amount = float(input("Enter Amount : ")); rate = float(input("Enter rate of interest : "))
interest = amount*rate/100
print ("Amount: ", amount, "Interest: ", interest)
'''
# Practice:
#   1. Print Person Details: (Name, City, Email, Phone)
#   2. Input and print Car Details (Company, Color, Mileage, year)
#   3. print Pet Details:[ Penname, Pet type(Dog/Cat/Bird/Fish),Color, Age, Price]
#   4. print Book Details(Book title, Author, price, year)
#   5. Print product details Name, price, qty
#   6. print bill amount ,Tax including
#   7. Print Student Details (Name, RollNo,(Marks1, Marks2, Marks3),Calculate total, avg.
#   8. Print fare of distance travelled.
#   9. Find simple interest(si) formula: SI = (PNR)/100;
#   10. Calculate aria of Square( SQA = side*side)
#   11. Rectangle area = length * breadth;
#   12. Triangle area = 1/2bh
#   13. Circle Area = (PI *r*r)
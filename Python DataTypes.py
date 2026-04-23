'''Built-in Data Types
In programming, data type is an important concept.
Variables can store different types of data. Each type of data used in
different ways. Ex: text data, numarical data, alphanumerical data.
Python has the following data types built-in by default, in these categories:
Text Type: str
Numeric Types: int, float, complex
Sequence Types: list, tuple, range
Mapping Type: dictSet Types: set, frozenset
Boolean Type: Bool True,False
Binary Types: bytes, bytearray, memoryview

Setting the Specific Data Type
If you want to specify the data type, you can use the following constructor
functions:
x = "Hello World" //str
x = 20 //int
x = 20.5 //float
x = 1j //complex
x = ["apple", "banana", "cherry"] //list
x = ("apple", "banana", "cherry") //tuple
x = range(6) //range
x = {"name" : "John", "age" : 36} //dict
x = {"apple", "banana", "cherry"} //set
x = frozenset({"apple", "banana", "cherry"}) //frozenset
x = True //bool
x = b"Hello" //bytes
x = bytearray(5) //bytearray
x = memoryview(bytes(5)) //memoryview

Getting the Data Type
You can get the data type of any variable by using the type() function:
Example
'''
x = 5
print(type(x))

# Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
x = 1
y = 35656222554887711
z = -3255522
print(type(x))
print(type(y))
print(type(z))

# Float can also be scientific numbers with an "e" to indicate the power of 10
x = 35e3
y = 12E4
z = -87.7e100
print(type(x))
print(type(y))
print(type(z))

# Complex numbers are written with a "j" as the imaginary part:
x = 3+5j
y = 5j
z = -5j
print(type(x))
print(type(y))
print(type(z))

num1 = 5
print(num1, 'is of type', type(num1))
num2 = 2.0
print(num2, 'is of type', type(num2))
num3 = 1+2j
print(num3, 'is of type', type(num3))

'''Random Number
Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:
Example
Import the random module, and display a random number between 1 and 9:
'''
import random
print(random.randrange(1, 10))

'''Python Casting
Converting one data type to another is known as casting. Casting in python is performed using constructor functions:
 int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
 float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
 str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals
'''
# Integers:
x = int(1) # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
print(x)
print(y)
print(z)

# float:
x = float(1) # x will be 1.0
y = float(2.8) # y will be 2.8
z = float("3") # z will be 3.0
w = float("4.2") # w will be 4.2
print(x)
print(y)
print(z)

# Strings:
x = str("s1") # x will be 's1'
y = str(2) # y will be '2'
z = str(3.0) # z will be '3.0'print(x)
print(x)
print(y)
print(z)

# You can convert from one type to another with the int(), float(), and complex() methods:
# Example: Conversion.py
x = 1 # int
y = 2.8 # float
z = 1j # complex
#convert from int to float:
a = float(x)
#convert from float to int:
b = int(y)
#convert from int to complex:
c = complex(x)
'''print(a)
print(b)
print(c)
'''
print(type(a))
print(type(b))
print(type(c))

# Example: Add.py
# declare int variables
a = 5
b = 6
# Add two numbers
sum = a + b
# Display the sum
print( sum)

# Using different Data types in program
# Using Strings
# Example1:
name = 'Python'
print(name)
message = 'Python is Simple'
print(message)

# Example2:
# Print Concatenated Strings: We can also join two strings together inside the print() statement. For example,
print ('Python is ' + 'Awesome.')

'''Python Input statement
This will accept data from keyboard.
Example1: input.py
name = input('Enter your name: ')
age = input('Enter your age: ')
height = input('Enter your height: ')
# Display the details using Output(print) statement
print('Name: '+name)
print('Age: '+age)
print('Height: '+height)

Example2:
All numbers taken from keyboard are string type
Input.py
num = input('Enter a number: ')
print('You Entered:', num)
print('Data type of num:', type(num))
o/p:
Enter a number: 10
You Entered: 10
Data type of num: <class 'str'>

Example 3:
Add Two Numbers with User Input
To convert user input into a number we can use int() or float()
functions as:
typecast.py
a = input('Enter first number: ')
b = input('Enter second number: ')
# Add two numbers
#sum = int(a) + int(b) # adds two numbers
sum = a + b # combine two numbers sidebyside
# Display the sum
print(sum)

It can converted while inputting data
Example 4:
Typecast2.py
a = int(input("Enter first no" ))
b = int(input("Enter second no" ))
sum = a + b
print ( "first no = ", a )
print ( "second no=", b )
print ( "sum = ", sum )

Try:
Ex1:
Accept student details
rollno, name, marks1, marks2, marks3. And calculate total and average.
Ex2: Complete the given program
x = 5
y = 10
# To take inputs from the user
#x = input('Enter value of x: ')
#y = input('Enter value of y: ')
# create a temporary variable and swap the values
temp = x
x = y
y = temp
Ex3: Try the given examples.
1. Calculate area of circle formula : 2 .
2. Calculate area of square (side * side).
3. Accept year of birth from the keyboard and print How old he is.
4. Calculate cube of given number for input.
5. Accept person details firstName, lastName, email, phone print fullName ,
email, Phone with Labels.
6. Take Productname, prince, quantity from input print cost. Of the product.
7. Convert kilometres to miles: 1 mile =1.6 km. 7 km = ? miles.
Number of miles = Km/1.6.
8. Accept student marks m1,m2,m3 from keyboard and Calculate total and
avg. Print avg using float data type.
9. Take a rupees from keyboard and print dollars.
What you learn
 Built-in Data Types
 Getting the Data Type Setting the Specific Data Type
 Python Numbers
 Int
 Complex
 Type Conversion
 Random Number
 Python Casting

'''

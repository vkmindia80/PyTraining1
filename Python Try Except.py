# Python Try Except

# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The else block lets you execute code when there is no error.
# The finally block lets you execute code, regardless of the result of the tryand except blocks.
'''
Exception Handling
When an error occurs, or exception as we call it, Python will normally stop and
generate an error message.
These exceptions can be handled using the try statement:
Example
The try block will generate an exception, because x is not defined:

try:
    print(x)
except:
    print("An exception occurred")

Since the try block raises an error, the except block will be executed.
Without the try block, the program will crash and raise an error:
Example
This statement will raise an error, because x is not defined:

print(x)

Traceback (most recent call last):
File "demo_try_except_error.py", line 3, in <module>
print(x)
NameError: name 'x' is not defined
Many Exceptions
You can define as many exception blocks as you want, e.g. if you want to execute a
special block of code for a special kind of error:
Example
Print one message if the try block raises a NameError and another for other errors:

try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")

Else
You can use the else keyword to define a block of code to be executed if no errors
were raised:Example
In this example, the try block does not generate any error:

try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

try:
    print("Hello", name)
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

Finally
The finally block, if specified, will be executed regardless if the try block raises an
error or not.
Example

try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")

This can be useful to close objects and clean up resources:
Example
Try to open and write to a file that is not writable:

try:
    f = open("demofile.txt")
    try:
        f.write("Lorum Ipsum")
    except:
        print("Something went wrong when writing to the file") # f = open("demofile.txt", "w")
    finally:
        f.close()
except:
    print("Something went wrong when opening the file")

The program can continue, without leaving the file object open.
Raise an exception
As a Python developer you can choose to throw an exception if a condition occurs.
To throw (or raise) an exception, use the raise keyword.
Example
Raise an error and stop the program if x is lower than 0:

x = -1
if x < 0:
    raise Exception("Sorry, no numbers below zero")

o/p:
Traceback (most recent call last):
File "demo_ref_keyword_raise.py", line 4, in <module>
raise Exception("Sorry, no numbers below zero")
Exception: Sorry, no numbers below zero
The raise keyword is used to raise an exception.
You can define what kind of error to raise, and the text to print to the user.
Example
Raise a TypeError if x is not an integer:

x = "hello"
if not type(x) is int:
    raise TypeError("Only integers are allowed")

o/p:
Traceback (most recent call last):
File "demo_ref_keyword_raise2.py", line 4, in <module>
raise TypeError("Only integers are allowed")
TypeError: Only integers are allowed
Practice Examples
Python User-Defined Exception
# define Python user-defined exceptions

class InvalidAgeException(Exception):
    "Raised when the input value is less than 18"
    pass
# you need to guess this number
number = 18
try:
    input_num = int(input("Enter a number: "))
    if input_num < number:
        raise InvalidAgeException
    else:
        print("Eligible to Vote")
except InvalidAgeException:
    print("Exception occurred: Invalid Age")

Output
If the user input input_num is greater than 18,
Enter a number: 45
Eligible to Vote
If the user input input_num is smaller than 18,
Enter a number: 14
Exception occurred: Invalid AgeExample2
Customizing Exception Classes
'''
class SalaryNotInRangeError(Exception):
    """Exception raised for errors in the input salary.
    Attributes:
    salary -- input salary which caused the error
    message -- explanation of the error
    """
    def __init__(self, salary, message="Salary is not in (5000, 15000) range"):
        self.salary = salary
        self.message = message
        super().__init__(self.message)
salary = int(input("Enter salary amount: "))
if not 5000 < salary < 15000:
    raise SalaryNotInRangeError(salary)
'''
Run Code
Output
Enter salary amount: 2000
Traceback (most recent call last):
File "<string>", line 17, in <module>
raise SalaryNotInRangeError(salary)
__main__.SalaryNotInRangeError: Salary is not in (5000, 15000) range
'''
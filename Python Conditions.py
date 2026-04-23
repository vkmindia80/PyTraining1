'''Python supports the usual logical conditions from mathematics:
 Equals: a == b
 Not Equals: a != b
 Less than: a < b
 Less than or equal to: a <= b
 Greater than: a > b
 Greater than or equal to: a >= b
These conditions can be used in several ways, most commonly in "if
statements" and loops.

Syntax:
if <expr>:
<statement1>
<statement2>
Example
If statement:
a = 333
b = 200
if b > a:
    print ("b is greater than a")
else:  
    print ("a is greater than b")

a = 33
b = 333
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

# Short Hand If: If you have only one statement to execute, you can put it on the same line as the if statement.
Example
One line if statement:

a = 333
b = 33
if a > b: print("a is greater than b")

Short Hand If ... Else
If you have only one statement to execute, one for if, and one for else, you
can put it all on the same line:
Example
One line if else statement:

a = 2222
b = 330
print("A") if a > b else print("B")
# This technique is known as Ternary Operators, or Conditional Expressions

You can also have multiple else statements on the same line:
Example
One line if else statement, with 3 conditions:

a = 3333
b = 330
print("A") if a > b else print("=") if a == b else print("B")

Using And
The and keyword is a logical operator, and is used to combine conditional
statements:
Example
Test if a is greater than b, AND if c is greater than a:

a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")

Using Or
The or keyword is a logical operator, and is used to combine conditional
statements:
Example
Test if a is greater than b, OR if a is greater than c:

a = 200
b = 333
c = 50
if a > b or a > c:
    print("At least one of the conditions is True")

Nested If
You can have if statements inside if statements, this is
called nested if statements.
Example

x = 19
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

The pass Statementif statements cannot be empty, but if you for some reason have
an if statement with no content, put in the pass statement to avoid getting
an error.
Example
a = 33
b = 200
if b > a:
pass
Example1
x = 250
if x > 15:
    pass # No action needed if x is greater than 5
else:
    print("x is 5 or less")

Example2
'''
for i in range(5):
    if i == 3:
        pass # Skip this iteration without performing any action
    else:
        print(i)

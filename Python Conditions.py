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

for i in range(5):
    if i == 3:
        pass # Skip this iteration without performing any action
    else:
        print(i)

The Python Match Statement
Instead of writing many if..else statements, you can use the match statement.
The match statement selects one of many code blocks to be executed.
Syntax
match expression:
case x:
code block
case y:
code block
case z:
code block
This is how it works:
 The match expression is evaluated once.
 The value of the expression is compared with the values of each case.
 If there is a match, the associated block of code is executed.
The example below uses the weekday number to print the weekday name:
Use the underscore character _ as the last case value if you want a code block to
execute when there are not other matches:
Example

day = 8
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Looking forward to the Weekend")

Combine Values
Use the pipe character | as an or operator in the case evaluation to check for more
than one value match in one case:
Example

day = 4
match day:
    case 1 | 2 | 3 | 4 | 5: print("Today is a weekday")
    case 6 | 7: print("I love weekends!")

# or
day = 4
match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Today is a weekday")
    case 6 | 7:
        print("I love weekends!")

If Statements as GuardsYou can add if statements in the case evaluation as an extra condition-check:
Example

month = 9
day = 4
match day:
    case 1 | 2 | 3 | 4 | 5 if month == 4:
        print("A weekday in April")
    case 1 | 2 | 3 | 4 | 5 if month == 5:
        print("A weekday in May")
    case _:
        print("No match")

Code Examples
1. if Statement:
age = 25
if age >= 18:
print("You are eligible to vote.")

2. if-else Statement:
temperature = 15
if temperature > 25:
print("It's hot outside.")
else:
print("It's not too hot.")

3. if-elif-else Statement:
score = 85
if score >= 90:
print("Grade: A")
elif score >= 80:
print("Grade: B")
elif score >= 70:
print("Grade: C")
else:
print("Grade: F")

4. Example with Multiple Conditions and Logical Operators:is_student = True
has_discount_card = False
total_bill = 120
if is_student and total_bill > 100:
print("You get a 10% student discount on your large purchase!")
elif has_discount_card or total_bill > 50:
print("You qualify for a general discount.")
else:
print("No special discounts apply.")

Try:
A. Find a given number is Odd or Even –using If-else
B. Find a Given gender is male or female
C. Find a given number is positive or negative using short hand if
D. Find a person is eligible for vote or not, accept age from keyboard- use if else
E. Find a biggest number in 3 given numbers using nested if
F. Accept 3 subject marks find he is passed or Fail. If all 3 subjects above 35 he is passed using
and operator.
G. Accept rating from keyboard print Good Excellent or Average using short hand if.

Answers
A.
number = 15
if number%2 == 0:
print("It is Even.")
else:
print("It is Odd.")

B.
gender = "m"
if gender == "m":
print("Male");
else:
print("Female");

C.
number = 15
if number > 0:
print("+ve")
else:
print("-ve")

D.
age = 20
if age >= 18:
print("You are eligible to vote.")

E.
a = 15
b = 25
c = 35
if a>b and a>c:
print("a isBig.")
elif b>a and b>c:
print("b is Big.")
else:
print("c is Big.")

F.
M1 = 45
M2 = 25
M3 = 55
if M1 <35 or M2 <35 or M3<35 :
print("Fail.")

G.
number = 5
print("Excellent.") if number == 5 else print("Good.") if number >=3 else
print("Bad t.")

#make sure all conditions given in single line

Match-case.py

1. Basic Value Matching:
The most straightforward use is matching a simple expression against literal values
or variables.
Python
status_code = 200
match status_code:
case 200:
print("Success!")
case 404:
print("Not Found.")
case _: # Wildcard for any other case
print("An error occurred.")

2. Matching Multiple Values with | (OR):
You can match against multiple values in a single case using the | operator.
Python
day = "Tuesday"
match day:case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
print("It's a weekday.")
case "Saturday" | "Sunday":
print("It's the weekend!")

3. Matching with if Guards:
For more complex conditions, you can add an if clause to
a case statement. This if guard evaluates a boolean expression, and the case only
matches if both the pattern and the if guard are true.
Python
score = 95 #s = score
match score:
    case score if score >= 90:
        print("Grade A")
    case score if score >= 80:
        print("Grade B")
    case score if score >= 70:
        print("Grade C")
    case _:
        print("Grade F")

4. Matching with Capture Variables:
You can capture parts of the matched expression into variables for use within
the case block.
Python
point = (1, 2)
match point:
case (x, y):
print(f"X-coordinate: {x}, Y-coordinate: {y}")
'''

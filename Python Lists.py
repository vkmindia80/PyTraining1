'''mylist = ["apple", "banana", "cherry"]
print(mylist)

List
Lists are used to store multiple items in a single variable.
Lists are one of 4 built-in data types in Python used to store collections of
data, the other 3 are Tuple, Set and Dictionary, all with different qualities
and usage.
Lists are created using square brackets:
Example
Create a List:

thislist = ["apple", "banana", "cherry"]
print(thislist)
print(*thislist, sep=", ")
print(", ".join(thislist))
numeric_list = [1, 2, 3]
print("-".join(str(x) for x in numeric_list)) #outputs string 1-2-3

List Items
List items are ordered, changeable, and allow duplicate values.
List items are indexed, the first item has index [0], the second item has
index [1] etc.
Example

thislist = ["apple", "banana", "cherry"]
print(thislist[0])
print(thislist[2])

Ordered
When we say that lists are ordered, it means that the items have a defined
order, and that order will not change.
If you add new items to a list, the new items will be placed at the end of the
list.
Note: There are some list methods that will change the order, but in
general: the order of the items will not change.

Changeable
The list is changeable, meaning that we can change, add, and remove items
in a list after it has been created.

Allow Duplicates
Since lists are indexed, lists can have items with the same value:
Example
Lists allow duplicate values:

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

List Length
To determine how many items a list has, use the len() function:
Example
Print the number of items in the list:

thislist = ["apple", "banana", "cherry"]
print(len(thislist))

List Items - Data Types
List items can be of any data type:
Example
String, int and boolean data types:

list1 = ["apple", "banana", "cherry"] #string list
list2 = [1, 5, 7, 9, 3] #integers list
list3 = [True, False, False] #boolean list
print(type(list1[0]))

A list can contain different data types:
ExampleA list with strings, integers and boolean values:

list1 = [1, 2, 3, "apple", "banana"] #mixed type list
list2 = ["abc", 34, True, 40, "male"] #mixed type list
# print(type(list1[4]))
print(list1[:])
for i in list1:
    print (type(i))        

type()
From Python's perspective, lists are defined as objects with the data type
'list':
<class 'list'>
Example
What is the data type of a list?

mylist = ["apple", "banana", "cherry"]
print(type(mylist))

The list() Constructor
It is also possible to use the list() constructor when creating a new list.
Example
Using the list() constructor to make a List:

thislist = list(("apple", "banana", "cherry")) # note the double roundbrackets
print(thislist)

Python Collections (Arrays)
There are four collection data types in the Python programming language:
 List is a collection which is ordered and changeable. Allows duplicate members.
 Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
 Dictionary is a collection which is ordered** and changeable. No duplicate members.

*Set items are unchangeable, but you can remove and/or add items
whenever you like.
**As of Python version 3.7, dictionaries are ordered. In Python 3.6 and
earlier, dictionaries are unordered.
When choosing a collection type, it is useful to understand the properties of
that type. Choosing the right type for a particular data set could mean
retention of meaning, and, it could mean an increase in efficiency or security.
1. Python Lists
2. Access List Items
3. Change List Items
a. Add List Items
b. Remove List Items
4. Loop Lists
5. List Comprehension
6. Sort Lists
7. Copy Lists
8. Join Lists
9. List Methods
10. List Exercises
Access List Items
List items are indexed and you can access them by referring to the index
number:
Example: Print the second item of the list:

thislist = ["apple", "banana", "cherry"]
print(thislist[1])

Negative Indexing
Negative indexing means start from the end
-1 refers to the last item, -2 refers to the second last item etc.

Example
Print the last item of the list:

thislist = ["apple", "banana", "cherry"]
print(thislist[0]) # apple
print(thislist[-1]) #cherry
print(thislist[4]) #error

Range of Indexes(List slicing)
You can specify a range of indexes by specifying where to start and where to
end the range. It is also known as list slicing.
When specifying a range, the return value will be a new list(sublist) with the
specified items

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
. The basic syntax for list slicing is
thislist[start:stop:step].
 start (optional): The index where the slice begins (inclusive). Defaults to 0.

 stop (optional): The index where the slice ends (exclusive, the element at this index
is not included). Defaults to the end of the list.
 step (optional): The interval between elements. Defaults to 1.
Example
Return the third, fourth, and fifth item:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

Note: The search will start at index 2 (included) and end at index 5 (not
included).
Remember that the first item has index 0.
By leaving out the start value, the range will start at the first item:
Example
This example returns the items from the beginning to, but NOT including,
"kiwi":

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

By leaving out the end value, the range will go on to the end of the list:
Example
This example returns the items from "cherry" to the end:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

Range of Negative Indexes
Specify negative indexes if you want to start the search from the end of the
list:
Example
This example returns the items from "orange" (-4) to, but NOT including
"mango" (-1):

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1]) #start from -4th to excluding -1

Check if Item Exists
To determine if a specified item is present in a list use the in keyword:
Example
Check if "apple" is present in the list:

thislist = ["apple", "banana", "cherry"]
if "Apple" in thislist:
    print("Yes, 'apple' is in the fruits list")
else: 
    print("Not Found")

Change Item ValueTo change the value of a specific item, refer to the index number:
Example
Change the second item:

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
# ['apple', 'blackcurrant', 'cherry']

Change a Range of Item Values
To change the value of items within a specific range, define a list with the
new values, and refer to the range of index numbers where you want to
insert the new values:
Example
Change the values "banana" and "cherry" with the values "blackcurrant" and
"watermelon":

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist) # 1,2 are replaced

If you insert more items than you replace, the new items will be inserted
where you specified, and the remaining items will move accordingly:
Example
Change the second value by replacing it with two new values:

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

Note: The length of the list will change when the number of items inserted
does not match the number of items replaced.If you insert less items than you replace, the new items will be inserted
where you specified, and the remaining items will move accordingly:
Example
Change the second and third value by replacing it with one value:

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

Add List Items
Append Items
To add an item to the end of the list, use the append() method:
Example
Using the append() method to append an item:

thislist = ["apple", "banana", "cherry"]
thislist.append("orange") # appends at list end
print(thislist)

Insert Items
To insert a new list item, without replacing any of the existing values, we can
use the insert() method.
The insert() method inserts an item at the specified index:
Example1
Insert an item as the second position:

thislist = ["apple", "banana", "cherry"]
thislist.insert(0, "orange") # inserts at specific position
print(thislist)

Example2
Insert "watermelon" as the third item:

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

Note: As a result of the example above, the list will now contain 4 items.
Remove List Items
Remove Specified Item
The remove() method removes the specified item.
Example
Remove "banana":

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

Remove Specified Index
The pop() method removes the specified index.
Example
Remove the second item:

thislist = ["apple", "banana", "cherry"]
thislist.pop(1) # 1st index item removed
print(thislist)

If you do not specify the index, the pop() method removes the last item.
Example
Remove the last item:

thislist = ["apple", "banana", "cherry"]
thislist.pop() # last item removes
print(thislist)

The del keyword also removes the specified index:
Example
Remove the first item:

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

The del keyword can also delete the list completely.
Example
Delete the entire list:

thislist = ["apple", "banana", "cherry"]
del thislist #removes complete list from memory
print(thislist) #error

Clear the List
The clear() method empties the list.
The list still remains, but it has no content.
Example
Clear the list content:

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist) #[]

Loop Lists
Loop through a List
You can loop through the list items by using a for loop:
Example
Print all items in the list, one by one:

thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

Loop through the Index Numbers
You can also loop through the list items by referring to their index number.
Use the range() and len() functions to create a suitable iterable.
ExamplePrint all items by referring to their index number:

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    # print(thislist[i])
    print(i, thislist[i])

The iterable created in the example above is [0, 1, 2].
Using a While Loop
You can loop through the list items by using a while loop.
Use the len() function to determine the length of the list, then start at 0 and
loop your way through the list items by refering to their indexes.
Remember to increase the index by 1 after each iteration.
Example
Print all items, using a while loop to go through all the index numbers

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(i+1, thislist[i])
    i = i + 1

Looping Using List ComprehensionList Comprehension offers the shortest syntax for looping through lists:
Example
A short hand for loop that will print all items in a list:

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

List Comprehension
List comprehension offers a shorter syntax when you want to create a new
list based on the values of an existing list.
Example:
Based on a list of fruits, you want a new list, containing only the fruits with
the letter "a" in the name.
Without list comprehension you will have to write a for statement with a
conditional test inside:
Example

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)

With list comprehension you can do all that with only one line of code:
Example

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist) # ['apple', 'banana', 'mango']

The Syntax
newlist = [expression for item in iterable if condition == True]
The return value is a new list, leaving the old list unchanged.
Condition
The condition is like a filter that only accepts the items that valuate to True.
Example
Only accept items that are not "apple":

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print(newlist)
#['banana', 'cherry', 'kiwi', 'mango']

The condition if x != "apple" will return True for all elements other than
"apple", making the new list contain all fruits except "apple".
The condition is optional and can be omitted:
Example
With no if statement:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits]
print(newlist)
# ['apple', 'banana', 'cherry', 'kiwi', 'mango']

IterableThe iterable can be any iterable object, like a list, tuple, set etc.
Example
You can use the range() function to create an iterable:

newlist = [x for x in range(10)]
print (newlist)

Same example, but with a condition:
Example
Accept only numbers lower than 5:

newlist = [x for x in range(10) if x < 5]
print (newlist)

Expression
The expression is the current item in the iteration, but it is also the outcome,
which you can manipulate before it ends up like a list item in the new list:
Example
Set the values in the new list to upper case:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)

You can set the outcome to whatever you like:
Example
Set all values in the new list to 'hello':

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ['hello' for x in fruits]
print(newlist)

The expression can also contain conditions, not like a filter, but as a way to
manipulate the outcome:
Example
Return "orange" instead of "banana":

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

Sort List Alphanumerically
List objects have a sort() method that will sort the list alphanumerically,
ascending, by default:
Example
Sort the list alphabetically:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

Example
Sort the list numerically:

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

Sort Descending
To sort descending, use the keyword argument reverse = True:
Example
Sort the list descending:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

Example
Sort the list descending:

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

Customize Sort Function
You can also customize your own function by using the keyword
argument key = function.
The function will return a number that will be used to sort the list (the lowest
number first):
Example
Sort the list based on how close the number is to 50:

def myfunc(n):
    return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

Case Insensitive Sort
By default the sort() method is case sensitive, resulting in all capital letters
being sorted before lower case letters:
Example
Case sensitive sorting can give an unexpected result:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

Luckily we can use built-in functions as key functions when sorting a list.
So if you want a case-insensitive sort function, use str.lower as a key
function:
Example
Perform a case-insensitive sort of the list:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
# ["banana", "cherry", "Kiwi", "Orange"]

Reverse Order
What if you want to reverse the order of a list, regardless of the alphabet?The reverse() method reverses the current sorting order of the elements.
Example
Reverse the order of the list items:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
['cherry', 'Kiwi', 'Orange', 'banana']

Copy a List
You cannot copy a list simply by typing list2 = list1, because: list2 will only
be a reference to list1, and changes made in list1 will automatically also be
made in list2.
There are ways to make a copy, one way is to use the built-in List
method copy().
Example
Make a copy of a list with the copy() method:

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist) # ['apple', 'banana', 'cherry']

Another way to make a copy is to use the built-in method list().
Example
Make a copy of a list with the list() method:

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist) # ['apple', 'banana', 'cherry']

Join Two Lists
There are several ways to join, or combine, two or more lists in Python.
One of the easiest ways are by using the + operator.
Example
Join two list:

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3) # ['a', 'b', 'c', 1, 2, 3 ]

Another way to join two lists is by appending all the items from list2 into
list1, one by one:
Example
Append list2 into list1:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
    list1.append(x)
print(list1) # ['a', 'b', 'c', 1, 2, 3 ]

Or you can use the extend() method, which purpose is to add elements from
one list to another list:
Example
Use the extend() method to add list2 at the end of list1:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1) # ['a', 'b', 'c', 1, 2, 3]

Try : Find a given element is in list or not

list = [10, 20, 30]
key = 20
if key in list:
    print("found")
else:
    print("not found")
Overview of Lists
 Access List Items
 Change List Items
 Add List Items
 Remove List Items
 Loop Lists
 List Comprehension
 Sort Lists
 Copy Lists
 Join Lists
 List Methods
List MethodsList Reverence
Try:
my_list = [10, 20, 30, 40, 50, 60, 70, 80]
# Index: 0 1 2 3 4 5 6 7
# Neg Index:-8 -7 -6 -5 -4 -3 -2 -1
#Here are common slicing patterns:
#Get all items after a specific position:
print(my_list[2:])
# Output: [30, 40, 50, 60, 70, 80]
# Starts at index 2 (inclusive) and goes to the end.
#Get all items before a specific position:
print(my_list[:3])
# Output: [10, 20, 30]
# Starts from the beginning and stops before index 3
(exclusive).
Get items within a specific range:
print(my_list[1:4])
# Output: [20, 30, 40]
# Starts at index 1 and stops before index 4.
#Get every nth item (using step):print(my_list[::2])
# Output: [10, 30, 50, 70]
# Starts from beginning, goes to end, steps by 2.
Use negative indexing (from the end):
print(my_list[-3:])
# Output: [60, 70, 80]
# Gets the last three elements.
print(my_list[:-2])
# Output: [10, 20, 30, 40, 50, 60]
# Gets everything except the last two elements.
Reverse a list:
print(my_list[::-1])
# Output: [80, 70, 60, 50, 40, 30, 20, 10]
# A negative step reverses the list.
#Create a copy of the entire list:
new_list = my_list[:]
# Creates a shallow copy of the list.
#Modifying Lists with Slicing
#Slicing can also be used to modify the original list in-place
by assigning a new iterable to the slice.
#Learn By Example
#Replace elements:
my_list[1:3] = [25, 35]
# my_list becomes [10, 25, 35, 40, 50, 60, 70, 80]
# The assigned list can be a different length.
Insert elements (using an empty slice):
my_list[2:2] = [28, 32]
# Inserts [28, 32] at index 2 without removing existing elements.
# Delete elements:
del my_list[1:4]
# Removes elements from index 1 up to (but not including) index 4.
Collection comparisons’
https://www.youtube.com/watch?v=11WrzU81q68
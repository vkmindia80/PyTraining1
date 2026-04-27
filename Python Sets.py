'''Set
Sets are used to store multiple items in a single variable.
Set is one of 4 built-in data types in Python used to store collections of data,
the other 3 are List, Tuple, and Dictionary, all with different qualities and
usage.
A set is a collection which is unordered, unchangeable*, and unindexed.
* Note: Set items are unchangeable, but you can remove items and add
new items.
Sets are written with curly brackets{} or the set() constructor.
Example
Create a Set:
# Using curly braces

myset = {"apple", "banana", "cherry"}
print(myset)

my_set = {1, 2, 3, 4}
print(f"Set created with curly braces: {my_set}")

Note: Sets are unordered, so you cannot be sure in which order the items
will appear.
Set Items
Set items are unordered, unchangeable, and do not allow duplicate values.
Unordered
Unordered means that the items in a set do not have a defined order.
Set items can appear in a different order every time you use them, and
cannot be referred to by index or key.Unchangeable
Set items are unchangeable, meaning that we cannot change the items after
the set has been created.
Once a set is created, you cannot change its items, but you can remove
items and add new items.
Duplicates Not Allowed
Sets cannot have two items with the same value.
Example
Duplicate values will be ignored:

thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

Get the Length of a Set
To determine how many items a set has, use the len() function.
Example
Get the number of items in a set:

thisset = {"apple", "banana", "cherry"}
print(len(thisset))

Set Items - Data Types
Set items can be of any data type:Example
String, int and boolean data types:

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
print(set1)
print(set2)
print(set3)

A set can contain different data types:
Example
A set with strings, integers and boolean values:

set1 = {"abc", 34, True, 40, "male"}
print(set1)

type()
From Python's perspective, sets are defined as objects with the data type
'set':
<class 'set'>
Example
What is the data type of a set?

myset = {"apple", "banana", "cherry"}
print(type(myset))

The set() Constructor
It is also possible to use the set() constructor to create a set.
Example
Using the set() constructor to make a set:
# Using the set() constructor with a list

thisset = set(("apple", "banana", "cherry")) # note the double roundbrackets
print(thisset)

another_set = set([1, 2, 2, 3, 4])
print(f"Set created with set() constructor: {another_set}") #
# Duplicates are automatically removed

Python Collections (Arrays)
There are four collection data types in the Python programming language:
 List is a collection which is ordered and changeable. Allows duplicate members.
 Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
 Dictionary is a collection which is ordered** and changeable. No duplicate members.
*Set items are unchangeable, but you can remove items and add new items.

Access Set Items
Access Items
You cannot access items in a set by referring to an index or a key.
But you can loop through the set items using a for loop, or ask if a specified
value is present in a set, by using the in keyword.
Example
Loop through the set, and print the values:

thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)

Example2
Check if "banana" is present in the set:

thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

Add Set Items
Add Items
Once a set is created, you cannot change its items, but you can add new
items.
To add one item to a set use the add() method.
Example
Add an item to a set, using the add() method:

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

Add Sets
To add items from another set into the current set, use the update() method.
Example
Add elements from tropical into thisset:

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

Add Any Iterable
The object in the update() method does not have to be a set, it can be any
iterable object (tuples, lists, dictionaries etc.).
Example
Add elements of a list to at set:

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

Remove Set Items
Remove Item
To remove an item in a set, use the remove(), or the discard() method.
Example1Remove "banana" by using the remove() method:

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

Note: If the item to remove does not exist, remove() will raise an error.
Example2
Remove "banana" by using the discard() method:

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

Note: If the item to remove does not exist, discard() will NOT raise an error.
You can also use the pop() method to remove an item, but this method will
remove the last item. Remember that sets are unordered, so you will not
know what item that gets removed.
The return value of the pop() method is the removed item.
Example3
Remove the last item by using the pop() method:

thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

Note: Sets are unordered, so when using the pop() method, you do not know
which item that gets removed.
Example4
The clear() method empties the set:

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

Example5
The del keyword will delete the set completely:

thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)

Python - Loop Sets
Loop Items
You can loop through the set items by using a for loop:
Example
Loop through the set, and print the values:

thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)

Python - Join Sets
Join Two Sets
There are several ways to join two or more sets in Python.
You can use the union() method that returns a new set containing all items
from both sets, or the update() method that inserts all the items from one set
into another:
ExampleThe union() method returns a new set with all items from both sets:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

Example2
The update() method inserts the items in set2 into set1:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

Set Overview
 Python Sets
 Access Set Items
 Add Set Items
 Remove Set Items
 Loop Sets
 Join Sets
 Set Methods
Set Methods Ref
Practice Example:
Set-add-remove.py
my_set = {1, 2, 3}
my_set.add(4)
print(f"After adding 4: {my_set}")
my_set.update([5, 6])
print(f"After updating with [5, 6]: {my_set}")
my_set.remove(2)
print(f"After removing 2: {my_set}")
my_set.discard(7) # No error if 7 is not present
print(f"After discarding 7: {my_set}")popped_element = my_set.pop()
print(f"Popped element: {popped_element}, Set after pop: {my_set}")
my_set.clear()
print(f"After clearing: {my_set}")
set-operations.py
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
# Union
union_set = set_a.union(set_b)
print(f"Union of A and B: {union_set}") # or set_a | set_b
# Intersection
intersection_set = set_a.intersection(set_b)
print(f"Intersection of A and B: {intersection_set}") # or set_a & set_b
# Difference (elements in A but not in B)
difference_set = set_a.difference(set_b)
print(f"Difference (A - B): {difference_set}") # or set_a - set_b
# Symmetric Difference (elements in A or B but not both)
symmetric_difference_set = set_a.symmetric_difference(set_b)
print(f"Symmetric difference: {symmetric_difference_set}") # or set_a ^ set_b
o/p:
 Union of A and B: {1, 2, 3, 4, 5, 6}
 Intersection of A and B: {3, 4}
 Difference (A - B): {1, 2}
 Symmetric difference: {1, 2, 5, 6}
set-example2.py
# create a set of integer type
student_id = {112, 114, 116, 118, 115}
print('Student ID:', student_id)
# create a set of string type
vowel_letters = {'a', 'e', 'i', 'o', 'u'}
print('Vowel Letters:', vowel_letters)
# create a set of mixed data types
mixed_set = {'Hello', 101, -2, 'Bye'}
print('Set of mixed data types:', mixed_set)
# using add() methodnumbers = {21, 34, 54, 12}
print('Initial Set:',numbers)
numbers.add(32)
print('New Set:', numbers)
# using update() method
companies = {'Lacoste', 'Ralph Lauren'}
tech_companies = ['apple', 'google', 'apple']
companies.update(tech_companies)
print(companies)
# Output: {'google', 'apple', 'Lacoste', 'Ralph Lauren'}
# remove 'Java' from a set
languages = {'Swift', 'Java', 'Python'}
print('Initial Set:',languages)
removedValue = languages.discard('Java')
print('Set after remove():', languages)
fruits = {"Apple", "Peach", "Mango"}
# for loop to access each fruits
for fruit in fruits:
print(fruit)
even_numbers = {2,4,6,8}
print('Set:',even_numbers)
# find number of elements
print('Total Elements:', len(even_numbers))
 o/p
Set: {8, 2, 4, 6}
Total Elements: 4
Ouputs:
Student ID: {112, 114, 115, 116, 118}
Vowel Letters: {'i', 'u', 'o', 'a', 'e'}
Set of mixed data types: {'Hello', 'Bye', 101, -2}
Initial Set: {34, 12, 21, 54}
New Set: {32, 34, 12, 21, 54}
{'Ralph Lauren', 'Lacoste', 'apple', 'google'}
Initial Set: {'Java', 'Python', 'Swift'}Set after remove(): {'Python', 'Swift'}
Peach
Apple
Mango
Set: {8, 2, 4, 6}
Total Elements: 4

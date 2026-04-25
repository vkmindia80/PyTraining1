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
'''
thislist = ["apple", "banana", "cherry"]
print(thislist)
print(*thislist, sep=", ")
print(", ".join(thislist))
numeric_list = [1, 2, 3]
print("-".join(str(x) for x in numeric_list)) #outputs string 1-2-3
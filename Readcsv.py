# Readcsv.py
'''
import csv
with open('innovators1.csv', 'r') as file:
    reader = csv.reader(file)
for row in reader:
    print(row)
'''
import csv
file = open ('innovators1.csv', 'r')
reader = csv.reader(file)
for row in reader:
    print(row)

'''Note: You can only remove empty folders.
More Practice Examples
File-handling.py
1. Creating and Writing to a File:
# Open a file in write mode ('w'). If the file doesn't exist, it will
be created.
# If it exists, its content will be truncated (emptied).
with open("my_file.txt", "w") as file:
file.write("This is the first line.\n")
file.write("This is the second line.\n")
print("Content written to my_file.txt")
2. Reading from a File:
# Open a file in read mode ('r').
with open("my_file.txt", "r") as file:
content = file.read() # Read the entire content
print("Entire file content:")
print(content)
# Reading line by line
with open("my_file.txt", "r") as file:
print("\nReading line by line:")
for line in file:print(line.strip()) # .strip() removes leading/trailing
whitespace, including newlines
3. Appending to a File:
# Open a file in append mode ('a'). Content will be added to the end.
with open("my_file.txt", "a") as file:
file.write("This line is appended.\n")
print("\nContent appended to my_file.txt")
# Verify the appended content
with open("my_file.txt", "r") as file:
print("File content after appending:")
print(file.read())
'''
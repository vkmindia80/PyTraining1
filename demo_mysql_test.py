# demo_mysql_test.py
'''
import mysql.connector
mydb = mysql.connector.connect(
host="localhost",
user="root",
password="Krishna@79"
)
print(mydb)

# create a database named "mydatabase":
import mysql.connector
mydb = mysql.connector.connect(
host="localhost",
user="root",
password="Krishna@79"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE mydatabase")

# Return a list of your system's databases:
import mysql.connector
mydb = mysql.connector.connect(
host="localhost",
user="root",
password="Krishna@79"
)
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)

# Try connecting to the database "mydatabase":
import mysql.connector
mydb = mysql.connector.connect(
host="localhost",
user="root",
password="Krishna@79",
database="mydatabase"
)

Creating a Table
To create a table in MySQL, use the "CREATE TABLE" statement.
Make sure you define the name of the database when you create the connection
Example

# Create a table named "customers":
import mysql.connector
mydb = mysql.connector.connect(
host="localhost",
user="root",
password="Krishna@79",
database="mydatabase"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

Check if Table Exists
You can check if a table exist by listing all tables in your database with the "SHOW
TABLES" statement:
Example

# Return a list of your system's databases:
import mysql.connector
mydb = mysql.connector.connect(
host="localhost",
user="root",
password="Krishna@79",
database="mydatabase"
)

mycursor = mydb.cursor()
mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)

Primary Key
When creating a table, you should also create a column with a unique key for each
record.
This can be done by defining a PRIMARY KEY.
We use the statement "INT AUTO_INCREMENT PRIMARY KEY" which will insert a
unique number for each record. Starting at 1, and increased by one for each record.
Example
Create primary key when creating the table:

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

If the table already exists, use the ALTER TABLE keyword:
Example
Create primary key on an existing table:

mycursor = mydb.cursor()
mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

Insert Into Table
To fill a table in MySQL, use the "INSERT INTO" statement.
Example
Insert a record in the "customers" table:

mycursor = mydb.cursor()
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val) # execute - executing sql code with one set of values
mydb.commit() # save
print(mycursor.rowcount, "record inserted.") # inserting record

Important!: Notice the statement: mydb.commit(). It is required to make the
changes, otherwise no changes are made to the table.
Insert Multiple Rows
To insert multiple rows into a table, use the executemany() method.
The second parameter of the executemany() method is a list of tuples, containing
the data you want to insert:
Example
Fill the "customers" table with data:

mycursor = mydb.cursor()
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
('Peter', 'Lowstreet 4'),
('Amy', 'Apple st 652'),
('Hannah', 'Mountain 21'),
('Michael', 'Valley 345'),
('Sandy', 'Ocean blvd 2'),
('Betty', 'Green Grass 1'),
('Richard', 'Sky st 331'),
('Susan', 'One way 98'),
('Vicky', 'Yellow Garden 2'),
('Ben', 'Park Lane 38'),
('William', 'Central st 954'),
('Chuck', 'Main Road 989'),
('Viola', 'Sideway 1633')
]
mycursor.executemany(sql, val) # executemany - executing sql code with multiple set of values
mydb.commit()
print(mycursor.rowcount, "was inserted.")

Get Inserted ID
You can get the id of the row you just inserted by asking the cursor object.
Note: If you insert more than one row, the id of the last inserted row is returned.
Example
Insert one row, and return the ID:

mycursor = mydb.cursor()
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Michelle", "Blue Village")
mycursor.execute(sql, val)
mydb.commit()
print("1 record inserted, ID:", mycursor.lastrowid)

Python MySQL Select From
Select From a Table
To select from a table in MySQL, use the "SELECT" statement:
Example
Select all records from the "customers" table, and display the result:

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

Note: We use the fetchall() method, which fetches all rows from the last executed
statement.
Selecting Columns
To select only some of the columns in a table, use the "SELECT" statement followed
by the column name(s):
Example
Select only the name and address columns:
'''
import mysql.connector
mydb = mysql.connector.connect(
host="localhost",
user="root",
password="Krishna@79",
database="mydatabase"
)
'''
mycursor = mydb.cursor()
mycursor.execute("SELECT name, id FROM customers")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

# retrieve the column names of a MySQL table
mycursor = mydb.cursor()
mycursor.execute("DESCRIBE customers")
for column in mycursor.fetchall():
    print(column[0])

Using the fetchone() Method
If you are only interested in one row, you can use the fetchone() method.
The fetchone() method will return the first row of the result:
Example
Fetch only one row:
import mysql.connector
mydb = mysql.connector.connect(
host="localhost",
user="yourusername",
password="yourpassword",
database="mydatabase"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchone()
print(myresult)

Select With a Filter
When selecting records from a table, you can filter the selection by using the
"WHERE" statement:Example
Select record(s) where the address is "Park Lane 38": result:

mycursor = mydb.cursor()
sql = "SELECT * FROM customers WHERE id ='15'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

Wildcard Characters
You can also select the records that starts, includes, or ends with a given letter or
phrase.
Use the % to represent wildcard characters:
Example
Select records where the address contains the word "way":

mycursor = mydb.cursor()
sql = "SELECT * FROM customers WHERE id LIKE '%1%'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

Prevent SQL Injection
When query values are provided by the user, you should escape the values.
This is to prevent SQL injections, which is a common web hacking technique to
destroy or misuse your database.
The mysql.connector module has methods to escape query values:
Example
Escape query values by using the placholder %s method:

mycursor = mydb.cursor()
sql = "SELECT * FROM customers WHERE id = %s"
# adr = ("Yellow Garden 2", )
id = (14,)
mycursor.execute(sql, id)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

Sort the Result
Use the ORDER BY statement to sort the result in ascending or descending order.
The ORDER BY keyword sorts the result ascending by default. To sort the result in
descending order, use the DESC keyword.
Example
Sort the result alphabetically by name: result:

mycursor = mydb.cursor()
sql = "SELECT * FROM customers ORDER BY name"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

# ORDER BY DESC
# Use the DESC keyword to sort the resul


mycursor = mydb.cursor()
sql = "SELECT * FROM customers ORDER BY name DESC"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

Display all names in descending order
Python MySQL Delete From By
Delete Record
You can delete records from an existing table by using the "DELETE FROM"
statement:
Example
Delete any record where the address is "Mountain 21":

mycursor = mydb.cursor()
sql = "DELETE FROM customers WHERE address = 'Mountain 21'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) deleted")

1 record(s) deletedImportant!: Notice the statement: mydb.commit(). It is required to make the
changes, otherwise no changes are made to the table.
Notice the WHERE clause in the DELETE syntax: The WHERE clause specifies
which record(s) that should be deleted. If you omit the WHERE clause, all records
will be deleted!
Prevent SQL Injection
It is considered a good practice to escape the values of any query, also in delete
statements.
This is to prevent SQL injections, which is a common web hacking technique to
destroy or misuse your database.
The mysql.connector module uses the placeholder %s to escape values in the delete
statement:
Example
Escape values by using the placeholder %s method:

mycursor = mydb.cursor()
sql = "DELETE FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )
mycursor.execute(sql, adr)
mydb.commit()
print(mycursor.rowcount, "record(s) deleted")

Python MySQL Drop Table
Delete a Table
You can delete an existing table by using the "DROP TABLE" statement:
Example
Delete the table "customers":

mycursor = mydb.cursor()
sql = "DROP TABLE customers"
mycursor.execute(sql)
#If this page was executed with no error(s), you have successfully deleted the "customers" table.

mycursor = mydb.cursor()
mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)

Drop Only if Exist
If the table you want to delete is already deleted, or for any other reason does not
exist, you can use the IF EXISTS keyword to avoid getting an error.
Example
Delete the table "customers" if it exists:

mycursor = mydb.cursor()
sql = "DROP TABLE IF EXISTS customers"
mycursor.execute(sql)
#If this page was executed with no error(s), you have successfully deleted the "customers" table.

Python MySQL Update Table
Update Table
You can update existing records in a table by using the "UPDATE" statement:
Example
Overwrite the address column from "Valley 345" to "Canyon 123":

mycursor = mydb.cursor()
sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
mydb.commit()
print(mycursor.rowcount, "record(s) affected")

mycursor = mydb.cursor()
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
('Peter', 'Lowstreet 4'),
('Amy', 'Apple st 652'),
('Hannah', 'Mountain 21'),
('Michael', 'Valley 345'),
('Sandy', 'Ocean blvd 2'),
('Betty', 'Green Grass 1'),
('Richard', 'Sky st 331'),
('Susan', 'One way 98'),
('Vicky', 'Yellow Garden 2'),
('Ben', 'Park Lane 38'),
('William', 'Central st 954'),
('Chuck', 'Main Road 989'),
('Viola', 'Sideway 1633')
]
mycursor.executemany(sql, val) # executemany - executing sql code with multiple set of values
mydb.commit()
print(mycursor.rowcount, "was inserted.")

Python MySQL Update Table
Update Table
You can update existing records in a table by using the "UPDATE" statement:
Example
Overwrite the address column from "Valley 345" to "Canyon 123":

mycursor = mydb.cursor()
sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")

1 record(s) affected
Important!: Notice the statement: mydb.commit(). It is required to make the
changes, otherwise no changes are made to the table.
Notice the WHERE clause in the UPDATE syntax: The WHERE clause specifies
which record or records that should be updated. If you omit the WHERE clause, all
records will be updated!
Prevent SQL Injection
It is considered a good practice to escape the values of any query, also in update
statements.
This is to prevent SQL injections, which is a common web hacking technique to
destroy or misuse your database.
The mysql.connector module uses the placeholder %s to escape values in the update
statement:
Example
Escape values by using the placeholder %s method:

mycursor = mydb.cursor()
sql = "UPDATE customers SET address = %s WHERE address = %s"
val = ("Valley 345", "Canyon 123")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")

mycursor = mydb.cursor()
sql = "select * from customers"
mycursor.execute(sql)
for x in mycursor:
    print(x)

Python MySQL LimitLimit the Result
You can limit the number of records returned from the query, by using the "LIMIT"
statement:
Example
Select the 5 first records in the "customers" table:

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM customers LIMIT 5")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

Start From Another Position
If you want to return five records, starting from the third record, you can use the
"OFFSET" keyword:Example
Start from position 3, and return 5 records:

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 5")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

Python MySQL Join
Join Two or More Tables
You can combine rows from two or more tables, based on a related column between
them, by using a JOIN statement.
Consider you have a "users" table and a "products" table:

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255), fav VARCHAR(255))")
mydb.commit()
print(mycursor.rowcount, "record(s) affected")

mycursor = mydb.cursor()
sql = "INSERT INTO users (name, address, fav) VALUES (%s, %s, %s)"
val = [
('Peter', 'Lowstreet 4', '152'),
('Amy', 'Apple st 652', '151'),
('Hannah', 'Mountain 21', '151'),
('Michael', 'Valley 345', '153'),
('Sandy', 'Ocean blvd 2', '154'),
('Betty', 'Green Grass 1', '155'),
('Richard', 'Sky st 331', '152'),
('Susan', 'One way 98', '153'),
('Vicky', 'Yellow Garden 2', '154'),
('Ben', 'Park Lane 38', '155'),
('William', 'Central st 954', '153'),
('Chuck', 'Main Road 989', '152'),
('Viola', 'Sideway 1633', '151')
]
mycursor.executemany(sql, val) # executemany - executing sql code with multiple set of values
mydb.commit()
print(mycursor.rowcount, "was inserted.")

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE products (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), favID INT)")
mydb.commit()
print(mycursor.rowcount, "record(s) affected")

mycursor = mydb.cursor()
sql = "INSERT INTO products (name, favID) VALUES (%s, %s)"
val = [
('Chocolate Heaven', '151'),
('Tasty Lemons', '152'),
('Apple Cider', '153'),
('Dubai Chocolate','154'),
('Vanilla Dreams','155')
]
mycursor.executemany(sql, val) # executemany - executing sql code with multiple set of values
mydb.commit()
print(mycursor.rowcount, "was inserted.")

These two tables can be combined by using users' fav field and products' id field.
Example
Join users and products to see the name of the users favorite product:

mycursor = mydb.cursor()
sql = "SELECT \
users.name AS user, \
products.name AS favorite \
FROM users \
INNER JOIN products ON users.fav = products.favID"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

Note: You can use JOIN instead of INNER JOIN. They will both give you the same
result.
LEFT JOIN
In the example above, Hannah, and Michael were excluded from the result, that is
because INNER JOIN only shows the records where there is a match.
If you want to show all users, even if they do not have a favorite product, use the
LEFT JOIN statement:
Example
Select all users and their favorite product:

mycursor = mydb.cursor()
sql = "SELECT \
users.name AS user, \
products.name AS favorite \
FROM users \
LEFT JOIN products ON users.fav = products.favID"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

RIGHT JOIN
If you want to return all products, and the users who have them as their favorite,
even if no user have them as their favorite, use the RIGHT JOIN statement:Example
Select all products, and the user(s) who have them as their favorite:
'''
mycursor = mydb.cursor()
sql = "SELECT \
users.name AS user, \
products.name AS favorite \
FROM users \
RIGHT JOIN products ON users.fav = products.favID"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

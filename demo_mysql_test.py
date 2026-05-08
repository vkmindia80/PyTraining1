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
'''
mycursor = mydb.cursor()
sql = "SELECT * FROM customers ORDER BY name"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

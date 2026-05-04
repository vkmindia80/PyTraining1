# Python Datetime
'''
Python Dates
A date in Python is not a data type of its own, but we can import a module
named datetime to work with dates as date objects.
Example
Import the datetime module and display the current date:
'''
import datetime
x = datetime.datetime.now()
print(x)
'''
Date Output
When we execute the code from the example above the result will be:
2025-03-05 14:04:48.867107
The date contains year, month, day, hour, minute, second, and microsecond.
The datetime module has many methods to return information about the date
object.
Here are a few examples, you will learn more about them later in this chapter:
Example
Return the year and name of weekday:
'''
import datetime
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))
'''
Creating Date Objects
To create a date, we can use the datetime() class (constructor) of
the datetime module.
The datetime() class requires three parameters to create a date: year, month, day.
Example
Create a date object:
'''
import datetime
x = datetime.datetime(2020, 5, 17)
print(x)
print(x.year)
print(x.day)
print(x.strftime("%A"))
'''
The strftime() Method
The datetime object has a method for formatting date objects into readable strings.The method is called strftime(), and takes one parameter, format, to specify the
format of the returned string:
Example
Display the name of the month:
'''
import datetime
x = datetime.datetime(2018, 6, 1)
print(x.strftime("%A"))
print(x.strftime("%B"))
print(x.strftime("%C"))

# Example
# @ Get the current date using today()
from datetime import date
# today() to get current date
todays_date = date.today()
print("Today's date =", todays_date)

'''
Output
Today's date = 2022-12-27
Get the date from a timestamp
A UNIX timestamp is the number of seconds between a particular date and January 1, 1970, at UTC.
You can convert a timestamp to a date using the fromtimestamp() method.
'''
from datetime import date
timestamp = date.fromtimestamp(1326244364)
print("Date =", timestamp)
'''
Output
Date = 2012-01-11
==============================
Print today's year, month and day
'''
from datetime import date# date object of today's date
today = date.today()
print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)
# Print hour, minute, second and microsecond
from datetime import time
a = time(11, 34, 56)
print("Hour =", a.hour)
print("Minute =", a.minute)
print("Second =", a.second)
print("Microsecond =", a.microsecond)

'''
Output
Hour = 11
Minute = 34
Second = 56
Microsecond = 0
Time duration in seconds
We can get the total number of seconds in a timedelta object using the
total_seconds() method.
'''
from datetime import timedelta
t = timedelta(days = 5, hours = 1, seconds = 33, microseconds = 233423)
print("Total seconds =", t.total_seconds())

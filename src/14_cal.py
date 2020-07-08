"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime

#date time expects an integer
#.Calendar(firstweeday=0)

#note: check argv, and others 
# argv_length = len(sys.argv)
# sys.argv.__len__()

#   - if no input, 
#       default to todays date. print method datetime.now().month and another with year.
#   - elif one input, 
#        its going to be the month and were going to use the current year. 
#   - elif two inputs, 
#        the first will be the month, 2nd will be the year. will use those for the calendar.
#   - else more than two inputs, 
#        send error message.

num_args = len(sys.argv)

if num_args == 1:
  month = datetime.now().month
  year = datetime.now().year

elif num_args == 2:
  year = datetime.now().year
  month = int(sys.argv[1])

elif num_args == 3:
  year = datetime.now().year
  month = int(sys.argv[1])

else:
  print("usage: 14_cal.py [month] [year]")

  sys.exit(1)

cal = calendar.TextCalendar()
cal.prmonth(year, month)

# what_month = input("what month?: ")
# what_year = input("what year?: ")

# if not what_month and not what_year:
#     print('Today date: ', datetime.now().month, datetime.now().year)
# elif what_month and not what_year:
#     print('Your date is: ', what_month, datetime.now().year)
# elif what_month and what_year:
#     print('Your date is: ', what_month, what_year)
# else:
#     print("please put in the correct data")


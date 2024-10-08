"""
Exercise 1:
Write a Python program that prints the current date and time using the datetime module.
"""

from datetime import datetime
my_dt = datetime.now() #Prints the current date and time 
print(my_dt)

"""
Exercise 2:
Write a Python program that prints the current date and time using the datetime module.
Using the strftime function format the date in standard U.S. date format (MM/DD/YYYY)
"""


my_string = "10/7/2024"
my_time = datetime.now() 

my_date = datetime.strftime(my_string, "%m/%d/%Y") #Formats the current date and prints the time

print(my_date)
print(my_time)

"""
Exercise 3:
Using the strptime function, convert two strings into dates.
Then find the difference in days between the two.
"""

my_string1 = "04/23/1994"
my_string2 = "12/4/2023"

my_date1 = datetime.strptime(my_string1, "%m/%d/%Y")
my_date2 = datetime.strptime(my_string2, "%m/%d/%Y")

print(my_date1)
print(my_date2)

print(my_date2 - my_date1) #Finds the difference in between the dates

"""
Excercise 4:
Write a program that asks the user for their birthdate and calculates their current 
age using the datetime module.
"""

print("Please enter your birthdate in mm/dd/yyyy format.") #User enters birthday in american format
user_date = input()
user_date = datetime.strptime(user_date, "%m/%d/%Y") #Formats it to calcalute current age
age = ((my_dt - user_date)/365)
print("You are " + str(age) + " years old.")



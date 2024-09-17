"""
TASK 1:
Create a float variable, and then convert it to an integer
Print both the original variable and the converted integer.
"""

random_number = 10.34
print(int (random_number)) #Used the int() function to convert into whole number. 
print(random_number)




"""
TASK 2:
Write code that takes a number as input and prints whether 
it's positive, negative, or zero using if-elif-else statements.
"""

num = int(input("Enter a Number: ")) #Used if statements to predict a number
if num > 0:
    print("Positive Number")
elif num == 0:
    print("Zero")
else:
    print("Negative Number")



"""
TASK 3:

Write code that takes two numbers as input (an integer and a float), 
performs addition, subtraction, multiplication, and division, and prints the results.
"""
my_number1 = int(input("Enter an integer: ")) #Used two numbers and printed results
my_number2 = float(input("Enter a float: "))

addition = my_number1 + my_number2
subtraction = my_number1 - my_number2
multiplication = my_number1 * my_number2
division = my_number1 / my_number2

print("Addition" , addition)
print("Subtraction:", subtraction)
print("Multiplication:" , multiplication)
print("Division:", division)




"""
TASK 4:

Create a dictionary with keys as fruit names and values as their respective quantities. 
Then print out the quantity of one of the fruits.
"""
fruits_inventory = {  #Created a dict. and printed apples
   'grapes':14,
   'apples':18
}
print(fruits_inventory['apples']) 

"""
TASK 5:

Create a string variable with that is a list of numbers and convert that string into a tuple.
Then print out the both the original string and tuple.
"""

general_string = "4,5,6,9,6,5"
my_tuple = tuple(map(int, general_string.split(", "))) #split the string and turned into a tuple

print("Original String:" , general_string)
print("Converted tuple:" , my_tuple)



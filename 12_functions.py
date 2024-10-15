"""
Task 1: Greeting
Write a function that takes a name as a 
agrument and prints a greeting message like "Hello, [name]!".
"""

def function_1(name):
    print("Hello + name!")
function_1("Arion") #Prints a name as a argument

"""
Task 2: Square of a Number
Write a function that takes an integer as an argument and returns its square.
"""

def number_function(int):
    return int * int #Square of a number and returns

print(number_function(9))

"""
Task 3: Even or Odd
Write a function that takes a number as a argument that 
returns `True` if the number is even, and `False` otherwise.
"""

def number2_function(number):
    if number % 2 == 0: #Evem or odd
        return True
    else: 
        return False

"""
Task 4: Area of a Rectangle
Write a function that takes the length and width of a rectangle and returns its area.
"""

def rec_area(length,width): 
    return length * width
print(rec_area(3,4)) #Area of a rectangle and returns it

"""
Task 5: Celsius to Fahrenheit
Write a function that takes a temperature in Celsius and returns 
the equivalent temperature in Fahrenheit using the correct formula
"""

def random_temp(celcius):
    fahrenheit = (celcius * (9/5)) + 32
    return fahrenheit

print(random_temp(45)) #Random Temp in celcius and then return it in fahrenheit


"""
Task 6: Average of Numbers
Write a function that takes a list of numbers as an argument
and returns the average (mean) of those numbers.
"""
random_list = [24, 0, 56, 1203, 54, 67, 1]

def avg_mean(random_list):
    sum = 0
    for x in random_list:
        sum += x
        return sum/len(random_list)
print(avg_mean(random_list)) #Finds the average mean of the list
        

"""
Task 7: Total Calculator
Create a function that has arguments for the price and quantity of something, 
and returns the total.

Your function should also optionally accept a 3rd argument for discount as a float, 
and return the discounted if provided.
"""

def store_calculator(price, quantity, discount = 1.0):
    return (price * quantity) * discount
print(store_calculator(10,5, 0.3)) #Does the price, how much and the discount



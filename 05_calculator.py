import math
print("Welcome to Arion's Calculatinator-inator 9000")

#Asks user to enter their two numbers
number_1= float(input("Enter your first number: "))
number_2 = float(input("Enter your second number: "))

#The setup for all operations
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def divide_2(num1, num2):
    return num1 // num2

def exponential(num1, num2):
    return num1 ** num2

def remainder(num1, num2):
    return num1 % num2

#Asks user to select an operation
print("Please select operation: " 
        "1. Add " 
        "2. Subtract " 
        "3. Multiply " 
        "4. Divide "
        "5. Floor Division "
        "6. Exponential "
        "7. Remainder ")


# Take input from the user and does the operation
select = int(input("Select operations from 1, 2, 3, 4, 5, 6, 7 : "))

if select == 1:
    print(number_1, "+", number_2, "=",
                    add(number_1, number_2))

elif select == 2:
    print(number_1, "-", number_2, "=",
                    subtract(number_1, number_2))

elif select == 3:
    print(number_1, "*", number_2, "=",
                    multiply(number_1, number_2))

elif select == 4:
    print(number_1, "/", number_2, "=",
                    divide(number_1, number_2))

elif select == 5:
    print(number_1, "//", number_2, "=",
                    divide_2(number_1, number_2))
    
elif select == 6: 
    print(number_1, "**", number_2, "=",
            exponential(number_1, number_2))
    
elif select == 7:
    print(number_1, "%", number_2, "=", 
          remainder(number_1, number_2))
           
else:
    print("Invalid input")


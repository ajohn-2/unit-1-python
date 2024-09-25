"""
Exercise 1:
Write a program to print numbers from 1 to 10 using a for loop.
"""
for x in range (1, 11): #Prints 1-10 using a for loop 
    print(x)


"""
Exercise 2:
Write a program to count by 10s from 900 to 1000
"""

for x in range(900, 1000, 10): #Counts by 10 from 900 to 1000
     print(x)

"""
Exercise 3:
Write a program that counts form 1-100 by 9
"""

for y in range(1, 100, 9): #Prints from 1-100 by 9
     print(y)

"""
Exercise 4:
Write a program to calculate the sum of all numbers from 1 to 10 using a for loop.
"""

numbers_total = 0
for x in range (1, 11): #Calculates the sum for all numbers from 1 to 10
    numbers_total += x
print(numbers_total)



"""
Excercise 5:
Uncomment the following code and run it. Then answer the following:
- What is the ouput of the code?

- Explain the iterative process that this code executes to get that output
"""

rows = 5

for i in range(rows):
    for j in range(i + 1):
         print('*', end=' ')
         print()

#The output of the code print an asteric almost an infinite amount of times. 
#The reason for ths iterative proces has to do with the "i+1" as that determines the amount of asterics. 
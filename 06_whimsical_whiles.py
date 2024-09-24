"""
1. Simple Counter:
Write a program that uses a while loop to print numbers from 1 to 10.
"""

x = 0

while x < 10: #Wrote a simple while loop and printed numbers from 1 to 10.
    x += 1
    print(x)

"""
2. Countdown:
Write a program that uses a while loop to print numbers from 10 to 1 in descending order.
"""

y = 10

while y > 0: #Reversing the code to a descending order
    print(y)
    y -= 1

"""
3. Factorial Calculation:
Write a program that calculates the factorial of a given number using a while loop.
"""
while True:
    n = 1
    factorial = 1
    num=int(input("Enter number: ")) #Calculates the factorials
    if num<=0:
        print("Incorrect")
        break
    while n<num:
        n+=1
        factorial*=n
    print(factorial)


"""
4. Password Guessing Game:
Create a simple password guessing game using a while loop. Ask the user to guess a predefined password and provide appropriate feedback.
"""

password = "henrydanger101"
guess = input("Guess the Password: ")

while guess != password:
    print("Incorrect Password")
    guess=input("Guess the Password: ") #Lets user guess the password

    print("Correct")
    



"""
5. Sum of Digits:
Write a program that calculates the sum of the digits of a given number using a while loop.
"""



"""
6. Fibonacci Series:
Write a program that prints the first n numbers in the Fibonacci sequence using a while loop.
"""

n = int(input("Enter a Number: "))
h = 0
b = 1

sum = h + b 

count = 1
print("Fibonacci series is: ", end=" ") #Lets User enter a number and it prints the fibonacci sequence
while (count <= n):
	count += 1
	print(h, end=" ")
	h = b
	b = sum
	sum = h + b

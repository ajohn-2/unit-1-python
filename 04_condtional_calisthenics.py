'''
Exercise 1:
Check if an integer is even and greater than 10.
Return True if both conditions are met, False otherwise.
'''

random_num = int[input("Enter a random integer: ")] #User enters a random number and checks if its evem and greater than 10
if random_num > 10 and random_num % 2 == 0:
    print("True")
else:
    print("False")


'''
Exercise 2:
Determine the ticket price based on age and student status.
Price is $10 if under 18 or a student, $20 otherwise.
'''

age = 18
student_stat = (input("Are you a Student?")) #Asks if they are a student and prints the price of ticket

if age <= 18 or student_stat:
    print("Price of ticket is $10")
else:
    print("Price of ticket is $20 ")


'''
Exercise 3:
Prompt the user to enter a fruit name. Check if the fruit is in the list. 
If it is, print "Yes, that fruit is in the list." 
If it's not, print "No, that fruit is not in the list."
'''
random_fruits = (input("Enter a Fruit: "))
fruits_lists = ["orange", "grapes", "pineapple "] #Checks if user entered fruits are in this list
    
if random_fruits != fruits_lists:
    print("Yes that fruit is in the list")
else:
    print("No, that fruit is not on the list")

'''
Exercise 4:
Check if a year is a century year and a leap year.
'''
random_year = int(input("Enter a random Year: ")) #User enters a random year and see if its both a century and leap year
if random_year % 400 == 0:
    print("It is a century year and a leap year") 
else:
    print("Not a century and leap year")


'''
Exercise 5:
Calculate the cost of shipping for an online order based on the order weight and destination zone. 
The shipping cost is $5 per kilogram for Zone A and $7 per kilogram for Zone B. 
If the order weight is less than 0 kg, return an error message.
'''

online_ord1 = int[input("The Order Weight is: ")]

if online_ord1 > 0:
    print("Error Invalid Input") #Online order shipping cost and zone

shipping_costA = 5.00
shipping_costB = 7.00

print ("Shipping Cost for Zone A is: ${online_ord1 *shipping_costA} and shipping cost for Zone B is: ${online_ord1*shipping_costB}")

'''
Exercise 6:
Determine the type of a triangle based on side lengths.
Equilateral, Isosceles, Scalene, or Not a triangle.
'''
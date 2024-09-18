"""
TASK 1:
Write code that checks if a user entered the correct password.
The password should not be case sensitive
"""

Password = "DoodleBobCrumb"
manual_pass = input("Enter Password: ").lower() #Enter a password and either prints correct or incorrect
if manual_pass == Password:
    print("Correct")
else:
    print("Incorrect")


"""
TASK 2:
Write code that checks if a user inputs an empty string
If the string is empty, print "invalid" otherwise print "valid"
"""

random_word = input("Something: ") #Empty string and prints it true
random_word = random_word.strip()
if bool(random_word) == True:
    print("Valid")
else:
    print("Invalid")




"""
TASK 3:

Write a program that will replace the word "cat" with the word "dog"
It should replace all occurances regardless of captilization 
"""
my_word = "Cat"
new_animal = my_word.replace("Cat", "Dog") #Replaced cat with dog 
print(new_animal)

"""
TASK 4:

Write a program that takes a person's name and age as input and prints it
"""

random_name = str(input("Enter your name: ")) #User enters name and age and prints it
random_age = int(input("Enter your age: "))

print(random_name , random_age)


"""
TASK 5:

Write a program that takes in two floats, and prints the quotient
The result should be rounded to the nearest tenth (1 decimal place)
"""


num_1 = float(input("Random Float: "))
num_2 = float(input("Enter another Random Float: "))

numb = num_1 / num_2 #Enter two floats and prints to the nearest tenth
txt = f"Result: {numb:.1f}" 
print("Quotient: " , numb)





"""
Exercise 1:
Write a program to print each character of a given string using a for loop.
"""
random_message = "Good Morning Pineapple" #Random string and prints each character 

for y in random_message:
    print(y)


"""
Exercise 2:
Write a program to calculate the sum of elements in a list using a for loop.
"""


numbers_list = [12, 13, 29, 34, 2]
total = 0 

for u in numbers_list: #For Loop sums up a list of nums 
    total += u
    print(total)

"""
Exercise 3:
Write a program to print the length of each word in a sentence using a for loop and a list.
"""

random_sentence = "Brownstone Dog Major"
new_sentence = random_sentence.split(" ")
sentence_sum = 0

for j in new_sentence: #Prints the length of each word 
    words_sum = len(j)
    print(words_sum)


"""
Excercise 4:
Write a program that creates a dictionary (atleast 4 key:value pairs) and then
iterates through a dictionary and prints the result



In a comment, answer the following, what do you notice about the output of your code?
Is it what you expected? 
"""
#I noticed that some of the outputs were not as expected but I know that python is different from other coding languages and that it can sometimes print something unexpected or different. 


food_inventory = { #Created a dictionary and prints the result 
    "carrots": 13,
    "lemons": 20,
    "salmon": 53, 
    "crossiant": 32
}

for x in food_inventory:
    print(x)

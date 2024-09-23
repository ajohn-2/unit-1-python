"""
Task 1: Create a list
Create a list with 4 elements and print it.
"""
random_list = ["Food", "Excersice", 345594 , "Walking"] #Random List and prints elements
print(random_list)

"""
Task 2: Add Element to a List
Add an element to the end of the list. Print the updated 
list.
"""

random_list1 = ["Carrots", 1948, "meds"] 
random_list1.append ("Green") #Adds an element to the random list
print(random_list1)

"""
Task 3: Remove Element from a List
Remove a specific element from the list. Print the 
updated list.

random_list4 = ["Temu", "Blue Giant", "yup"]
random_list4.remove("Temu") #Removes Temu from list 
print(random_list4)


"""

"""
Task 4: Modify Element in a List
Modify an element at a specific index with a new value. 
Print the updated list.
"""

random_list5 = ["Arion", 15, "Kale"] #Modifies a random list
random_list5


"""
Task 5: Append Multiple Elements to a List
Append multiple elements to the end of the list. Print 
the updated list.
"""
random_list9 = ["Carrots", 1948, "meds"] 
random_list9.append("Money")
random_list9.append("Lettuce") #Adds multiple elements to the end of the list
print(random_list9)


"""
Task 6: Delete Element at a Specific Index
Delete an element at a specific index. Print the updated 
list.
"""

my_list = ["Henry", 75 , "Yuppie", "Jayden" , "Health"]
del my_list[3] #Deletes an element at an index
print(my_list)


"""
Task 7: Subsetting lists
Create a new variable equal to the first 2 items of your list
Then print out the new variable
"""

places = ["Dubai", "New York City", "Budapest"]
print ( places[0:2] ) #Prints the subset of the first two items

"""
Task 8: Extend a List
Extend the list with the elements of another list. Print 
the updated list.
"""

foods_A = ["chicken", "watermelon" , "apple"]
foods_B = ["grapes", "cabbage", "carrots"] 

foods = foods_A + foods_B #Makes two lists and adds both together
print(foods)
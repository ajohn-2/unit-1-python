
with open("to_Dos.txt") as file:
     tasks = file.readlines() #Reads the file and opens the file 


while True:
    print("Your Current ToDo's are: ")
    print(tasks)
    print("Organize your tasks by add / remove / clear all / edit / display / exit") #Asks the user for their input
    option = input()

    if option == "add":
        next_todo = input("What would you like to add?") #Adding an item to their list
        tasks.append(next_todo + "\n")

    elif option == "remove":
        print(tasks)
        print("Please type in the todo # you want to remove") #Removes an item at a certain index 
        next_remove = int(input())
        del tasks [next_remove - 1]


    elif option == "Clear all":
       tasks.clear() #Clears all tasks


    elif option  == "Edit":
        print(tasks)
        print("Please type in the todo # you want to edit") #Allows user to edit at a certain index
        next_edit = int(input())
        print("Create a new task.")
        tasks[next_edit - 1] = input() 


    elif option == "Display":
        num = 1
        for x in tasks:
            print(f"{num}){x}") #Displays all tasks
            num += 1

    elif option == "exit":
        with open("to_Dos.txt", "w") as file:
            file.writelines(tasks) 
        break #Allows the user to exit the program
            




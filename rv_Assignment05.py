# ------------------------------------------------------------------------ #
# Title: Assignment 05_ToDoList
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# rvandercar,11/18/2020,Added/Edited code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)

objFile = open("ToDoList.txt", "r")
for row in objFile:
    txtdata = row.split(",")
    dicRow = {"Task": txtdata[0], "Priority": txtdata[1].strip()}
    lstTable.append(dicRow)
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks


    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print("This is the current to do list.")
        print("Row - Task - Priority")
        counter = 1
        for row in lstTable:
            print(f'{counter} | {row["Task"]} | {row["Priority"]} |')
            counter += 1
        continue

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        #elif (strChoice.strip() == '2'):
        try:
            newData = input("Add a new task and priority (Task, Priority): ")
            strData = newData.split(",")
            dicRow = {"Task": strData[0], "Priority": strData[1]}
            lstTable.append(dicRow)
            print("Task has been added.")
        except:
            print("Be sure to add a task and priority, separated by a comma!")
        continue

    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        remove = int(input("Which task would you like delete? (Put in row number): "))
        lstTable.pop(remove)

        print("Row",remove,"has been taken of your to do list")

        continue

    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):

        objFile = open("ToDoList.txtt","w")
        for row in lstTable:
            objFile.write(row["Task"] + "," + row["Priority"] + "\n")
        objFile.close()
        print("Your To Do List is now up to date.")
        continue


    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        strConfirmExit = input("Are you sure you want to exit the program? [Y/N] ")
        if strConfirmExit.lower().strip() == 'y':
            print("Now go get things done!")
            break
        else:
            continue
            # and Exit the program

    else:
        print("That is not a valid choice. Please enter a number between 1-5.")
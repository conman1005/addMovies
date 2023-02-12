#Authors: Conner Cullity and Matthias Mcnulty
#Date: 2023/02/05
#Purpose: Read, Write and Search in a csv file

#import csv for reader
import csv
#import os to enable clearing of the console
import os

# Functions!

# This function will prompt the user for input and append the information to a 
#   .csv file 
def add_book():
    
    #clear console - omit?
    # os.system('cls')

    #Prompt for new book details
    newTitle = input("Type book title to add: ")
    newAuthor = input("Enter the author of " + newTitle + ": ")
    isNumber = False
    newYear=""

    while isNumber == False:
        #prompt for book year
        newYear = input("Please enter the release year: ")
        try :
            #checks if string can be converted to integer, no need to actually convert to integer
            int(newYear)
            #if the error doesn't happen, you get to this part, setting inNumber to True and ending loop
            isNumber = True
            print("\nBook Successfully added.\n")
        except ValueError :
            #Prompts for proper input if input ins't a number
            print("Try again, please enter a Number for the Year.\n")

    #append new data
        rows.append([newTitle,newAuthor,newYear])

# This function will print the entire contents of a reading list savded to a .csv file
def print_books():
        #clear console
        os.system('cls')

        with open('book_list.csv', newline='') as file:
            reader = csv.reader(file)
            #get csv header
            header = []
            header = next(reader)
            header
            #get rows
            rows = []
            for row in reader:
                    rows.append(row)
                    print(row[0] + " was written by " + row[1] + " and was released in " + row[2] + "\n")
                    file.close
# This function allows the user to input the title of a book to be searched. The 
#   corresponding book information will be printed(title, author, year)
def search_books():
    # clear console
    os.system('cls')

    #prompt for book title
    search = input("Enter Book Title to Search: ")
    #boolean to let user know if the search found anything
    found = False
    #loop through each row and check if the title equals the search phrase.
    for row in rows:
        if row[0].lower() == search.lower():
            #if the search phrase equals any title than the details will be printed.
            print("\n" + row[0] + " was written by " + row[1] + " and was released in " + row[2] + "\n")
            found = True
    if found == False:
        print("There is no book in the database with the name " + search  + ", you can use the 'add book' command to add it.\n")

    else:
        os.system('cls')
        print("Please enter a valid command. The commands for this program are 'add book', 'printbooks', 'searchbooks' and 'exit'\n")




# omit ? - initially clear console to get rid of top text from program opening
# os.system('cls')

#initially read file
header = []
rows = []
with open('book_list.csv', newline='') as file:
    reader = csv.reader(file)
    #get csv header
    
    header = next(reader)
    # header
    #get rows
    for row in reader:
        rows.append(row)
    file.close

# main program
print('Welcome to the program!\n')

program_active = True
while program_active:

    menu_sub_program = True
    while menu_sub_program:

        print("The commands are: 'add book', 'print books', 'search books' and 'exit'")

        menu_command = input('please enter one of the above commands: ')
        
        if menu_command == ('add book'):
            menu_sub_program = False
            add_book()

        elif menu_command == ('print books'):
            menu_sub_program = False
            print_books()
        
        elif menu_command == ('search books'):
            menu_sub_program = False
            search_books()

        elif menu_command == ('exit'):
            menu_sub_program = False
            program_active = False
            



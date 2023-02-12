#Authors: Conner Cullity and Matthias Mcnulty
#Date: 2023/02/05
#Purpose: Read, Write and Search in a csv file

#import csv for reader
import csv
#import os to enable clearing of the console
import os


#initially clear console to get rid of top text from program opening
os.system('cls')

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

#loop program
loop = True
print("The commands for this program are: 'add book', 'print books', 'search books' and 'exit'\n")
while (loop):
    #Prompt for command
    command = input("Enter Command: ")
    #exit program if user enters 'exit'
    if command == "exit":
        loop=False
    elif command == "add book":
        #clear console
        os.system('cls')
        #Prompt for new book details
        newTitle = input("Type book title to add: ")
        newAuthor = input("Enter the author of " + newTitle + ": ")
        isNumber = False
        newYear=""
        #loop for number input
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

        with open('book_list.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["title","author","year"])
            for row in rows:
                writer.writerow(row)
            file.close
    elif command == "print books":
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
    elif command == "search books":
        #clear console
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
            print("There is no book in the database with the name " + search  + ", you can use the 'addBook' command to add it.\n")
    else:
        os.system('cls')
        print("Please enter a valid command. The commands for this program are 'addbook', 'printbooks', 'searchbooks' and 'exit'\n")
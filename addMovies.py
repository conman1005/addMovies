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
with open('movies.csv', newline='') as file:
    reader = csv.reader(file)
    #get csv header
    
    header = next(reader)
    header
    #get rows
    for row in reader:
        rows.append(row)
    file.close

#loop program
loop = True
print("The commands for this program are 'addMovie', 'printMovies', 'searchMovie' and 'exit'\n")
while (loop):
    #Prompt for command
    command = input("Enter Command: ")
    #exit program if user enters 'exit'
    if command == "exit":
        loop=False
    elif command == "addMovie":
        #clear console
        os.system('cls')
        #Prompt for new movie details
        newName = input("Type movie name to Add: ")
        newDirector = input("Type the Director for " + newName + ": ")
        isNumber = False
        newYear=""
        #loop for number input
        while isNumber == False:
            #prompt for movie year
            newYear = input("Please enter the release year: ")
            try :
                #checks if string can be converted to integer, no need to actually convert to integer
                int(newYear)
                #if the error doesn't happen, you get to this part, setting inNumber to True and ending loop
                isNumber = True
                print("\nMovie Successfully added.\n")
            except ValueError :
                #Prompts for proper input if input ins't a number
                print("Please enter a Number for the Year.\n")

        #append new data
        rows.append([newName,newDirector,newYear])

        with open('movies.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["title","director","year"])
            for row in rows:
                writer.writerow(row)
            file.close
    elif command == "printMovies":
        #clear console
        os.system('cls')
        with open('movies.csv', newline='') as file:
            reader = csv.reader(file)
            #get csv header
            header = []
            header = next(reader)
            header
            #get rows
            rows = []
            for row in reader:
                rows.append(row)
                print(row[0] + " was Directed by " + row[1] + " and was released in " + row[2] + "\n")
            file.close
    elif command == "searchMovie":
        #clear console
        os.system('cls')
        #prompt for movie title
        search = input("Enter Movie Title to Search: ")
        #boolean to let user know if the search found anything
        found = False
        #loop through each row and check if the title equals the search phrase.
        for row in rows:
            if row[0].lower() == search.lower():
                #if the search phrase equals any title than the details will be printed.
                print("\n" + row[0] + " was Directed by " + row[1] + " and was released in " + row[2] + "\n")
                found = True
        if found == False:
            print("There is no movie in the database with the name " + search  + ", you can use the 'addMovie' command to add it.\n")
    else:
        os.system('cls')
        print("Please enter a valid command. The commands for this program are 'addMovie', 'printMovies', 'searchMovie' and 'exit'\n")
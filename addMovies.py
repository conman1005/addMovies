#Authors: Conner Cullity and Matthias Mcnulty
#Date: 2023/02/05
#Purpose: Read and write to a csv file

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
        newYear = input("Pleas enter the release year: ")
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
    else:
        print("Please enter a valid command. The commands for this programds are 'addMovie', 'printMovies' and 'exit'")
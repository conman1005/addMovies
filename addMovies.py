
#import csv for reader
import csv
#open movies.csv file
movieFile = open("movies.csv")
type(movieFile)
#read the file
reader = csv.reader(movieFile)

#get csv header
header = []
header = next(reader)
header
#get rows
rows = []
for row in reader:
    rows.append(row)
print(rows)

#new movie
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
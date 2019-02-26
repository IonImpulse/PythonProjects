from math import *
from random import *
import csv

inputFile = "InputData.csv"

#Function to check if there are too many classes, too many people per class, or during the same time slot
def validate(list,referenceList,eReferenceList) :
    tempReferenceList = eReferenceList
    for rows in list :
        loopNum = 0
        for item in range(len(list[loopNum])-2) :
            item + 1
            loopNum += 1
    for rows in list :
        loopNum = 0
        for item in tempReferenceList :
            for key in item :
                if len(tempReferenceList[loopNum][key]) > 2 :
                    return False
            loopNum += 1
    return True

#Imports the data as a matrix, making sure to not just crash if the file isn't found
try:
    with open(inputFile, newline = "") as file :
        inputDataRaw =  [row for row in csv.reader(file)]
except Exception as e:
    print(str(e) + "\nCould not find file. Please rename the input file to \"InputData.csv\", and restart the program.")


#Gets the classes from the data, and maximumStudents
loopNum = 0
classInputList = []
while True :
    classInputList.append(inputDataRaw[loopNum][1])
    loopNum +=1
    if inputDataRaw[loopNum][0] == "Maximum:" :
        maximumStudents = int(inputDataRaw[loopNum][1])
        pos = loopNum
        break

#Converts it to a dict inside a list, as an easy way to determine how many of them there are
classReference = []
loopNum = 0

#Iterates over all of the class data, breaks it up, and counts duplicates
for i in classInputList :
    i = i.split(",")
    classReference.append({})
    for o in i :
        exists = False
        if len(classReference[loopNum]) > 0 :
            for p in classReference[loopNum] :
                if o[:4] == p[:4] :
                    classReference[loopNum][o[:4]] += 1
                    exists = True
        if exists == False :
            classReference[loopNum][o[:4]] = 1
    loopNum += 1


#Sets GOA classes to the maximum of 5, since there is no real "period" for it
loopNum = 0
for i in classReference :
    for item in i :
        if item == "GOA" :
            classReference[loopNum][item] = 5
    loopNum += 1

#Gets student groups from data, will continue looping until there is no more data
loopNum = pos + 1
studentsList = []
while True :
    studentsList.append([i for i in inputDataRaw[loopNum]])
    loopNum +=1
    try:
        row = inputDataRaw[loopNum][0]
    except Exception as e:
        break

#Creates an empty dict to keep track of classes
solves = []
loopNum = 0
eClassReference = classReference
for item in eClassReference :
    for key in item :
        eClassReference[loopNum][key] = 0
    loopNum += 1

#Start the solve. It starts at row A, then keeps going down, making changes until it is correct. If not, then it switches to the next row
loopNum = 0
for row in studentsList :
    print("Loop number: " + str(loopNum+1) + " out of " + str(len(studentsList)))
    tempSList = studentsList
    if validate(tempSList,classReference,eClassReference) == True :
        solves.append(tempSList)
    loopNum += 1

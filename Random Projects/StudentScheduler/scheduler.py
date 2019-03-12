from math import *
import csv
from copy import deepcopy
import itertools
import tkinter as tk
from tkinter import filedialog
import os
import sys
clear = lambda: os.system('cls')
root = tk.Tk()
root.withdraw()

#Simple file dialog, wiht csv set as default
inputFile = filedialog.askopenfilename(filetypes = (("Comma Seperated Values","*.csv"),("All files", "*.*")))

#Function to check if there are too many classes, too many people per class, or during the same time slot
def validate(list,referenceList,eReferenceList,maximum,eTeachList) :
    tempReferenceList = deepcopy(eReferenceList)
    tempTeacherList = deepcopy(eTeachList)
    tList = [[list[j][i] for j in range(len(list))] for i in range(len(list[0]))]
    tempLen = len(tList[0])
    del tList[0]
    del tList[-1]
    for columns in tList :
        print(columns)
        for i in range(tempLen-2) :
            loopNum1 = 0
            placed = False
            for o in tempReferenceList :
                for key in o :
                    if key == "GOA" :
                        placed = True
                    elif key[:5] == columns[i + 1][:5] and tempTeacherList[loopNum1] == False and placed == False:
                        tempTeacherList[loopNum1] = True
                        placed = True
                loopNum1 += 1
            if placed == False :
                print("26")
                print(tempTeacherList)
                return False
        print(tempTeacherList)
    tempReferenceList = deepcopy(eReferenceList)
    tempLen = len(list[0])
    for rows in list :
        print(rows)
        for i in range(tempLen-2) :
            loopNum1 = 0
            placed = False
            for o in tempReferenceList :
                for key in o :
                    if str(key[:4]) == str(rows[i + 1][:4]) and (tempReferenceList[loopNum1][key] + int(rows[tempLen-1])) <= maximum and placed == False :
                        tempReferenceList[loopNum1][key] += int(rows[tempLen-1])
                        placed = True
                loopNum1 += 1
            if placed == False :
                print("41")
                return False
    for rows in list :
        loopNum = 0
        for item in tempReferenceList :
            for key in item :
                if tempReferenceList[loopNum][key] > maximum :
                    print("51")
                    return False
            loopNum += 1
    return True

#Imports the data as  a matrix, making sure to not just crash if the file isn't found
try:
    with open(inputFile, newline = "") as file :
        inputDataRaw =  [row for row in csv.reader(file)]
except Exception as e:
    print(str(e) + "\n=====================================\nPlease select the appropriate CSV file.")
    sys.exit()


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
eClassReference = deepcopy(classReference)
for item in classReference :
    for key in item :
        if classReference[loopNum][key] > 1 :
            for i in range(classReference[loopNum][key]-1) :
                eClassReference[loopNum][str(key)+str(i+1)] = 0
        eClassReference[loopNum][key] = 0
    loopNum += 1

teacherList = []
for i in eClassReference :
    teacherList.append(False)
#Start the solve. It starts at row A, then keeps going down, making changes until it is correct.
loopNum = 0
tempSList = []
restart = False
previous = 0
while loopNum < len(studentsList):
    if restart == False and previous != 120 :
        tempSList.append(studentsList[loopNum])
    print("Loop number: " + str(loopNum+1) + " out of " + str(len(studentsList)))
    loopNum2 = 0
    previous = 0
    tempPermutations = list(itertools.permutations(((tempSList[loopNum][1:])[:-1])))
    while validate(tempSList,classReference,eClassReference,maximumStudents,teacherList) == False and loopNum2 + previous < (len(tempPermutations)):
        if restart == True :
            tempSList[loopNum] = (list(studentsList[loopNum][0]) + list(tempPermutations[loopNum2 + previous]) + [int(studentsList[loopNum][len(studentsList[loopNum])-1])])
            clear()
            print("Permutation number " + str(loopNum2+previous))
            loopNum2 += 1
        if validate(tempSList,classReference,eClassReference,maximumStudents,teacherList) == False :
            restart = True
            previous += 1
        else :
            restart = False
            previous = 0
    if restart == False :
        loopNum += 1
if validate(tempSList,classReference,eClassReference,maximumStudents,teacherList) == True :
    solves.append(tempSList)
print("=======================================================")
for item in tempSList :
    print(item)

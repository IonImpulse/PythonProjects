#Use https://github.com/tsudoko/pullcord to download discord logs in the correct CSV format.
#I haven't even started to code it yet, but I'm 99% sure this will have plenty of bugs in it.
import csv
import tkinter as tk
from tkinter import filedialog
from time import sleep
import os
import sys

clear = lambda: os.system('cls')
root = tk.Tk()
user = os.environ.get('USERNAME')
root.withdraw()

def progress(count, total, status=''):
    bar_len = 50
    filled_len = int(round(bar_len * count / float(total)))
    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)
    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
    sys.stdout.flush()

def makeWords(inputString, removePunc = True) :
    if removePunc == True :
        inputString = inputString.replace(",", "")
        inputString = inputString.replace(".", "")
        inputString = inputString.replace("!", "")
        inputString = inputString.replace("?", "")
        inputString = inputString.replace("\"", "")
        inputString = inputString.replace("*", "")
    inputString = ''.join(inputString).split()
    return inputString

#Input section
inputDir = filedialog.askdirectory()

print(inputDir)
filesList = os.listdir(inputDir)
dataSet = []

print("Files found:")
for index, file in enumerate(filesList) :
    print(str(index) + ": " + str(file))

input()
for i in filesList :
    if i[-3:] == "csv" :
        try:
            tempInputString = inputDir + "\\" + i
            with open(tempInputString, newline = "", encoding="utf8") as file :
                dataSet.append([])
                dataSet[len(dataSet)-1] =  [row for row in csv.reader(file, delimiter = ';')]
                dataSet[len(dataSet)-1] =  dataSet[len(dataSet)-1][1:]
        except Exception as e:
            print(str(e) + "\n=====================================\nThere was a problem opening \"" + str(i) + "\".")
            print("Exiting in 5 seconds...")
            sleep(5)
            sys.exit()

#Parser to database
userList = []
userQuotes = {}
wordList = []
wordCount = {}

for index, i in enumerate(dataSet) :
    clear()
    progress(index, len(dataSet), status='Parsing text')
    for j in i :
        #user part
        if j[0] not in userList :
            userList.append(j[0])
            userQuotes[j[0]] = []
        if j[2] != "" :
            userQuotes.setdefault(j[0], []).append(j[2])

        #word part
        tempWordList = makeWords(j[2])
        for k in tempWordList :
            if k not in wordList :
                wordList.append(k)
                wordCount[k] = 0
            wordCount[k] += 1
clear()
#Database to statistics
userListWords = {}
userListCharacters = {}
userWordCount = {}
userVocab = []
userVocabCount = []
userMessageCount = {}

for index, i in enumerate(userQuotes) :
    userListWords[userList[index]] = 0
    userListCharacters[userList[index]] = 0
    for j in userQuotes[i] :
        userListCharacters[userList[index]] += sum(len(k) for k in makeWords(j, False))
        userListWords[userList[index]] += len(makeWords(j))

for index, i in enumerate(userQuotes.items()) :
    userVocab.append([])
    userVocabCount.append({})
    userMessageCount[userList[index]] = 0
    userWordCount[userList[index]] = 0
    for j in i[1] :
        userMessageCount[userList[index]] += 1
        tempWordList = makeWords(j)
        userWordCount[userList[index]] += len(tempWordList)
        for k in tempWordList :
            if k not in userVocab[index] :
                userVocab[index].append(k)
                userVocabCount[index][k] = 0
            userVocabCount[index][k] += 1

wordCountSorted = sorted(wordCount.items(), key = lambda x: x[1], reverse = True)
userMessageCountSorted = sorted(userMessageCount.items(), key = lambda x: x[1], reverse = True)
userListCharactersSorted = sorted(userListCharacters.items(), key = lambda x: x[1], reverse = True)
userWordCount = sorted(userWordCount.items(), key = lambda x: x[1], reverse = True)
userVocabCountSorted = []
for index, i in enumerate(userVocabCount) :
    userVocabCountSorted.append({})
    userVocabCountSorted[index] = sorted(userVocabCount[index].items(), key=lambda x: x[1], reverse = True)

#Save Function
print("Enter save name:")
saveName = input(":")
exportPath = "C:\\Users\\" + str(user) + "\\Documents\\DiscordData\\" + str(saveName) + "\\"
if os.path.exists(exportPath) == False :
    os.makedirs(exportPath)

with open(exportPath + "Server.csv", "w", newline='', encoding="utf8") as target :
    csv_writer = csv.writer(target, dialect="excel")
    csv_writer.writerow(["Statistics for: " + str(saveName)])

    csv_writer.writerow(["-----------------------------"])
    csv_writer.writerow(["List of Users:"])
    csv_writer.writerow(["-----------------------------"])
    for i in userList :
        csv_writer.writerow([i])

    csv_writer.writerow(["-----------------------------"])
    csv_writer.writerow(["Message Count per User"])
    csv_writer.writerow(["-----------------------------"])
    csv_writer.writerows(userMessageCountSorted)

    csv_writer.writerow(["-----------------------------"])
    csv_writer.writerow(["Word Count per User"])
    csv_writer.writerow(["-----------------------------"])
    csv_writer.writerows(userWordCount)

    csv_writer.writerow(["-----------------------------"])
    csv_writer.writerow(["Character Count per User"])
    csv_writer.writerow(["-----------------------------"])
    csv_writer.writerows(userListCharactersSorted)

    csv_writer.writerow(["-----------------------------"])
    csv_writer.writerow(["Word Count"])
    csv_writer.writerow(["-----------------------------"])
    csv_writer.writerows(wordCountSorted)

for index, i in enumerate(userList) :
    if os.path.exists(exportPath + "Users\\") == False :
        os.makedirs(exportPath + "Users\\")
    tempI = i.replace("/", "")
    tempI = tempI.replace("\\", "")
    tempI = tempI.replace(":", "")
    tempI = tempI.replace("?", "")
    tempI = tempI.replace("\"", "")
    tempI = tempI.replace("|", "")
    tempI = tempI.replace("<", "")
    tempI = tempI.replace(">", "")
    with open(exportPath + "Users\\" + str(tempI) + "-StatsCount.csv", "w", newline='', encoding="utf8") as target :
            csv_writer = csv.writer(target, dialect="excel")
            csv_writer.writerow(["Count per word of: " + str(i)])
            csv_writer.writerows(userVocabCountSorted[index])

#Include:
#-Top ten-fifty words on server - DONE
#-Sorted list of users by message - DONE
#-Sorted list of users by words - DONE
#-Sorted list of users by character -DONE
#-Top ten-fifty words per user - DONE

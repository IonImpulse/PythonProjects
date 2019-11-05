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

if os.path.exists("C:\\Users\\" + str(user) + "\\Documents\\DiscordData\\") == False :
    os.makedirs("C:\\Users\\" + str(user) + "\\Documents\\DiscordData\\")

def progress(count, total, status=''):
    bar_len = 50
    filled_len = int(round(bar_len * count / float(total)))
    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)
    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
    sys.stdout.flush()

def removePunc(inputString) :
    inputString = inputString.replace(",", "")
    inputString = inputString.replace(".", "")
    inputString = inputString.replace("!", "")
    inputString = inputString.replace("?", "")
    inputString = inputString.replace("\"", "")
    inputString = inputString.replace("*", "")
    return inputString

def makeWords(inputString, removePunct = True) :
    if removePunct == True :
        inputString = removePunc(inputString)
    inputString = ''.join(inputString).split()
    return inputString

def splitQuotes(inputString) :
    tempDashPos = inputString.find("-")
    tempSpacePos = inputString.find(" ", tempDashPos + 2)
    print(tempDashPos, tempSpacePos)
    try:
        if tempSpacePos == -1 :
            tempName = inputString[tempDashPos + 1:]
        else :
            tempName = inputString[tempDashPos + 1:tempSpacePos]
        print(tempName)
        outputString = inputString[:tempDashPos].replace('\"', '')
        print(outputString)
    except Exception as e:
        raise

    return [tempName, outputString]

#Input section
inputDir = filedialog.askdirectory()

print(inputDir)
filesList = os.listdir(inputDir)
dataSet = []

serverName = filesList[0][:filesList[0].index(" - ")]
print("==" + str(serverName) + "==")
print("Files found:")
for index, file in enumerate(filesList) :
    print(str(index) + ": " + str(file[file.index(" - ") + 3:]))

print("\nSelect quote channels? Y/n")
choice = input(":")

quoteChannels = []

if choice.lower() == "y" :
    moreQuotes = True
    while moreQuotes == True :
        print("Channel number?")
        quoteChannels.append(input(":"))
        if quoteChannels[-1] == "n" :
            moreQuotes = False
            del quoteChannels[-1]
        else :
            try:
                quoteChannels[-1] = int(quoteChannels[-1])
            except Exception as e:
                print("Input a number. Try again...")
                del quoteChannels[-1]

if len(quoteChannels) > 0 :
    quoteRawData = []
    nameList = []
    nameKey = {}
    quotesByUser = {}
    quotesByPoster = {}

    print("Load name-key file? Y/n")
    choice = input(":")

    if choice.lower() == "y" :
        nameKeyFile = filedialog.askopenfilename(filetypes = (("Plaintext","*.txt"),("All files", "*.*")))
        with open(nameKeyFile, 'r') as keyFile :
            nameKey = eval(keyFile.readline())
            print(nameKey)
            input()
    for i in quoteChannels :
        tempInputString = inputDir + "\\" + filesList[i]
        with open(tempInputString, newline = "", encoding="utf8") as file :
            quoteRawData += [row for row in csv.reader(file, delimiter = ';')][1:]

    rowNumber = 0
    quoteOutput = []
    while rowNumber < len(quoteRawData) :
        row = quoteRawData[rowNumber]
        if row[0] not in quotesByPoster :
            quotesByPoster[row[0]] = []

            if row[0] not in nameKey :
                clear()
                print("Real name not found. Please enter name for \"" + str(row[0]) + "\"")
                tempName = input(":")
                nameKey[row[0]] = tempName

            quotesByUser[nameKey[row[0]]] = []

        splitRow = splitQuotes(row[2])

        if splitRow[0] != '' :
            if splitRow[0] not in nameList :
                nameList.append(splitRow[0])

            if splitRow[1].replace(' ', '') == '' and row[3] != '' :
                quoteOutput.append([row[0], splitRow[0], row[3]])
            elif  splitRow[1].replace(' ', '') == '' :
                quoteOutput[-1] = [quoteOutput[-1][0], splitRow[0], quoteOutput[-1][2]]
            else :
                quoteOutput.append([row[0], splitRow[0], splitRow[1]])
        else :
            if row[3] != '' :
                quoteOutput.append([row[0], "", row[3]])
            else :
                quoteOutput.append([row[0], "", row[2]])

        rowNumber += 1

    with open("C:\\Users\\" + str(user) + "\\Documents\\DiscordData\\namekey.txt", 'w') as keyFile :
        print(nameKey, file=keyFile)

    for i in range(len(quoteOutput)) :
        print(i)
        for j in range(2) :
            quoteOutput[i][j] = quoteOutput[i][j].replace('\"', '')

    print(nameKey)
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
    csv_writer.writerow(["Statistics for: " + str(serverName)])

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

if os.path.exists(exportPath + "Users\\") == False :
    os.makedirs(exportPath + "Users\\")
for index, i in enumerate(userList) :
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



if len(quoteChannels) > 0 :
    if os.path.exists(exportPath + "Quotes\\") == False :
        os.makedirs(exportPath + "Quotes\\")

    with open(exportPath + "Quoteboard.csv", "w", newline='', encoding="utf8") as target :
        pass

    for index, i in enumerate(nameList) :
        with open(exportPath + "Quotes\\" + str(removePunc(i)) + "-Quotes.csv", "w", newline='', encoding="utf8") as target :
            csv_writer = csv.writer(target, dialect="excel")
            csv_writer.writerow(["Quotes of " + str(removePunc(i))])
            for j in quoteOutput :
                if removePunc(j[1].lower()) == removePunc(i.lower()) :
                    csv_writer.writerow([j[2], "Quoted by " + str(nameKey[j[0]])])
#Include:
#-Top ten-fifty words on server - DONE
#-Sorted list of users by message - DONE
#-Sorted list of users by words - DONE
#-Sorted list of users by character -DONE
#-Top ten-fifty words per user - DONE

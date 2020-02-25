from nltk.corpus import wordnet
import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()
import sys

def my_print(text):
    sys.stdout.write(str(text) + "\n")
    sys.stdout.flush()

def getSyn(inputWord) :
    outList = []
    for syn in wordnet.synsets(inputWord):
        for l in syn.lemmas():
            outList.append(l.name())
    return list(set(outList))

inputFile = filedialog.askopenfilename(filetypes = (("Text File","*.txt"),("All files", "*.*")))

file = open(inputFile, "r", newline = "\n")

rawInputData = file.readlines()

vocab = [i.lower()[:i.rfind("\t")] for i in rawInputData]
total = len(vocab) - 1

synonyms = []

for i in range(total) :
    my_print(str(i) + " out of " + str(total))
    tempList = getSyn(vocab[i])
    synonyms.append(tempList)
    top = len(tempList) - 1
    for j in range(top) :
        synonyms[i] += getSyn(tempList[j])
    
    synonyms[i] = list(set(synonyms[i]))


choice = ""

while(choice.lower() != "exit") :
    print("Word?")
    choice = input(":").lower()

    top20 = []

    inputSynList = getSyn(choice)
    top = len(inputSynList) - 1

    for i in range(top) :
        tempList = getSyn(inputSynList[i])
        for j in tempList :
            inputSynList.append(j)

    print(inputSynList)
    for index, synonymList in enumerate(synonyms) :
        print(synonymList)
        wordCount = 0

        for syn in inputSynList :
            if choice in synonymList :
                wordCount += 100
            if syn in synonymList :
                wordCount += 1

        if wordCount > 0 :
            if len(top20) > 0 :
                if top20[0][0] < wordCount :
                    top20.append([wordCount, index])
                    top20 = sorted(top20, key = lambda x: int(x[0]), reverse=False)
                    print(top20)
                if len(top20) > 20 :
                    del top20[20]
            else  :
                top20.append([wordCount, index])
    
    top20 = sorted(top20, key = lambda x: int(x[0]), reverse=True)
    for i in top20 :
        print(vocab[i[1]], i[0])
    print("\n")
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

def clean_word(word) :
    word = word.replace(" ", "").replace(",", "").replace(".", "").replace(":", "").replace("\"", "")

    return word.lower()
def getChanges(input_word) :
    top20 = []

    inputSynList = getSyn(input_word)
    top = len(inputSynList) - 1

    for i in range(top) :
        tempList = getSyn(inputSynList[i])
        for j in tempList :
            inputSynList.append(j)

    for index, synonymList in enumerate(synonyms) :
        wordCount = 0

        for syn in inputSynList :
            if input_word in synonymList :
                wordCount += 100
            if syn in synonymList :
                wordCount += 1

        if wordCount > 0 :
            if len(top20) > 0 :
                if top20[0][0] < wordCount :
                    top20.append([wordCount, vocab[index]])
                    top20 = sorted(top20, key = lambda x: int(x[0]), reverse=False)
                if len(top20) > 20 :
                    del top20[20]
            else  :
                top20.append([wordCount, vocab[index]])
    
    top20 = sorted(top20, key = lambda x: int(x[0]), reverse=True)
    return top20

inputFile = filedialog.askopenfilename(filetypes = (("Text File","*.txt"),("All files", "*.*")))

changeFile = filedialog.askopenfilename(filetypes = (("Text File","*.txt"),("All files", "*.*")))
file = open(inputFile, "r", newline = "\n")

rawInputData = file.readlines()

file = open(changeFile, "r", newline = "\n")

rawChangeData = file.readlines()

changeData = []

for line in rawChangeData :
    temp = line.split(". ")

    for i in temp :
        if i != "\r\n" :    
            changeData.append(i)


print(changeData)
vocab = []

for index, i in enumerate(rawInputData) :
    if i.replace(" ", "")[:9] != "antonyms:" and len(i) > 2:
        vocab.append(i.lower()[:i.rfind("\t")])

total = len(vocab) - 1


print(vocab)
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

words_to_change = []

for l_pos, line in enumerate(changeData) :
    for w_pos, word in enumerate(line.split(" ")) :
        print(clean_word(word))
        possible_changes = getChanges(clean_word(word))
        
        if len(possible_changes) > 0 :
            print("\n")
            print(line)
            print("Word on line " + str(l_pos) + ", word " + str(w_pos) + "")
            print("Change [" + str(word) + "] to:")
            print("0: No Change")

            for index, i in enumerate(possible_changes) :
                print(str(index + 1) + ": " + str(i))

            selection = -1

            while selection == -1 :
                choice = input(":")
                try : 
                    selection = int(choice)
                    if selection > len(possible_changes) :
                        print("Please input a valid number")
                        selection = -1

                except Exception as e :
                    print("Please input a valid number")

            if selection != 0 :
                words_to_change.append([word, possible_changes[selection-1], l_pos, w_pos])

for i in words_to_change :
    print(i)
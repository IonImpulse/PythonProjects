import csv
import tkinter as tk
from tkinter import filedialog
import os
clear = lambda: os.system('cls')
root = tk.Tk()
user = os.environ.get('USERNAME')
root.withdraw()

def findSmallest(data,iteration) :
    smallest = sorted(data, key = lambda x: x[iteration])
    return(smallest[iteration])

inputFile = filedialog.askopenfilename(filetypes = (("Comma Seperated Values","*.csv"),("All files", "*.*")))
try:
    with open(inputFile, newline = "") as file :
        inputDataRaw =  [row for row in csv.reader(file)]
except Exception as e:
    print(str(e) + "\n=====================================\nPlease select the appropriate CSV file.")
    print("Exiting in 5 seconds...")
    sleep(5)
    sys.exit()

candidates = []
for i in range(len(inputDataRaw[0])-1) :
    candidates.append(inputDataRaw[0][i+1][:-1][inputDataRaw[0][i+1].index("[")+1:])
voteList = []
for i in range(len(candidates)) :
    voteList.append([])
    for j in candidates :
        voteList[i].append(0)

votes = inputDataRaw[1:]
for index, i in enumerate(votes) :
    for j in range(len(i)-1) :
        voteList[j][int(i[j+1])-1] += 1
for i in voteList :
    print(i)
selected = False

for index, i in enumerate(voteList) :
    if i[0] > len(votes) :
        selected = candidates[index]
        print("The winner is: " + str(selected))
        exit()
while selected == False :
    print(findSmallest(voteList,0))

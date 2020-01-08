import csv
import requests
import tkinter as tk
from tkinter import filedialog
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

inputFile = filedialog.askopenfilename(filetypes = (("Comma Seperated Values","*.csv"),("All files", "*.*")))
outputDirectory = os.path.dirname(inputFile)

if os.path.exists(outputDirectory) == False :
    os.makedirs(outputDirectory)

imagePrefix = "IMG_"

print("Start at message:")
start = input(":")

with open(inputFile, newline = "", encoding="utf8") as file :
    fileRawData = [row for row in csv.reader(file, delimiter = ';')]

requestList = [[],[],[]]

fileRawData = fileRawData[0:]

for index, i in enumerate(fileRawData) :
    if i[3] != "" :
        requestList[0].append(i[0])
        requestList[1].append(i[1])
        requestList[2].append(i[3])

counter = 0
for index, j in enumerate(requestList[2]) :
    tempURLS = j.split(',')
    print("Message " + str(index + 1) + " out of " + str(len(requestList[2])))
    print("Found " + str(len(tempURLS)) + " photo(s)")
    for i in tempURLS :
        try:
            if index >= int(start) :
                tempImg = requests.get(i)
                outputPath = outputDirectory + '\\' + imagePrefix + str(counter) + '.' + tempImg.url.split('.')[-1]
                open(outputPath, 'wb').write(tempImg.content)
            counter += 1
        except Exception as e:
            print(e)
            print("Could not get photo #" + str(i))

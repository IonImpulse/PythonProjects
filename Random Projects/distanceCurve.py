import math
import tkinter as tk
from tkinter import filedialog
import csv

def getDistanceBad(origin, destination) :
    lat1, lon1 = origin
    lat2, lon2 = destination

    d = math.sqrt(((lat2-lat1)**2) + ((lon2-lon1)**2))

    return d

def angleFromCoordinate(lat1, long1, lat2, long2) :
    x = lat2 - lat1
    y = long2 - long1

    angle = (math.atan2(y,x))

    return angle

root = tk.Tk()
root.withdraw()

inputFile = filedialog.askopenfilename(filetypes = (("Comma Seperated Values","*.csv"),("All files", "*.*")))

with open(inputFile, newline = "") as file :
    inputDataRaw = [row for row in csv.reader(file)]

total = 0
angle = False

direction = angleFromCoordinate(float(inputDataRaw[0][0]),float(inputDataRaw[0][1]), float(inputDataRaw[1][0]), float(inputDataRaw[1][1]))
for i in range(len(inputDataRaw) - 1) :
    total += getDistanceBad((float(inputDataRaw[i][0]),float(inputDataRaw[i][1])), (float(inputDataRaw[i + 1][0]), float(inputDataRaw[i + 1][1])))
    angle += abs(angleFromCoordinate(float(inputDataRaw[i][0]),float(inputDataRaw[i][1]), float(inputDataRaw[i + 1][0]), float(inputDataRaw[i + 1][1])))

print("Total Curve: " + str(angle) + " Degrees")
print("Average Curve: " + str(angle/total) + " Degrees")
crow = getDistanceBad((float(inputDataRaw[0][0]),float(inputDataRaw[0][1])), (float(inputDataRaw[-1][0]),float(inputDataRaw[-1][1])))
print("Length: " + str(total))
print("Crow Flys: " + str(crow))
try :
    print("Ratio " + str(crow/total))
except Exception as e :
    print("Ratio Division by Zero")

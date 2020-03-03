from geopy.distance import geodesic
from geopy.geocoders import Nominatim
import csv
import tkinter as tk
from tkinter import filedialog
from time import sleep

def getLocation(inLocation, timeoutNum = 10) :
    if timeoutNum != 0 :
        try:
            location = geolocator.geocode(inLocation)
        except Exception as e:
            location = getLocation(inLocation, timeoutNum - 1)
    else :
        print("Timeout, waiting 1 minute")
        sleep(60)
        location = getLocation(inLocation)
    return location

root = tk.Tk()
root.withdraw()

geolocator = Nominatim(user_agent="edv121@outlook.com", timeout=5)

location = getLocation("160 John St, Seattle, WA 98109")
The_Downtown_School_A_Lakeside_School = (location.latitude, location.longitude)

inputFile = filedialog.askopenfilename(filetypes = (("Comma Seperated Values","*.csv"),("All files", "*.*")))

with open("inputFile", newline = "") as file :
    inputDataRaw = [row for row in csv.reader(file)]

total = len(inputDataRaw)
print("Grabbed file with " + str(total) + " colleges. Starting geopy requests...")

outputTable = [["Name","Address","Distance from DTS"]]

for index, school in enumerate(inputDataRaw) :
    if index % 100 == 0 :
        with open("OutputDistances.csv", "w", newline = "") as file :
            csv_writer = csv.writer(file, dialect='excel')
            for i in outputTable:
                csv_writer.writerow(i)    
            outputTable = []
    
    if school[2] == "Institution" :
        location = getLocation(school[1])
        
        if location != None :
            location = (location.latitude, location.longitude)
            distance = geodesic(The_Downtown_School_A_Lakeside_School, location).miles
            print(str(index) + "out of " + str(total) + "\nLocation: " + school[0] + "\nDistance: " + str(distance))
            print("")
            outputTable.append([school[0], school[1], distance])
        else :
            print("Skipping " + school[0])
            print("")

with open("OutputDistances.csv", "w", newline = "") as file :
    csv_writer = csv.writer(file, dialect='excel')
    for i in outputTable:
        csv_writer.writerow(i)
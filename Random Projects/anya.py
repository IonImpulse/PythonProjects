import censusgeocode as cg
import csv
import tkinter as tk
from tkinter import filedialog
from time import sleep
import math
import os

def getDistance(origin, destination):
    """
    Calculate the Haversine distance.

    Parameters
    ----------
    origin : tuple of float
        (lat, long)
    destination : tuple of float
        (lat, long)

    Returns
    -------
    distance_in_miles : float

    Examples
    --------
    >>> origin = (48.1372, 11.5756)  # Munich
    >>> destination = (52.5186, 13.4083)  # Berlin
    >>> round(distance(origin, destination), 1)
    504.2
    """
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 6371  # km

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat / 2) * math.sin(dlat / 2) +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
         math.sin(dlon / 2) * math.sin(dlon / 2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = radius * c * 0.6213712

    return d

root = tk.Tk()
root.withdraw()

#location = cg.onelineaddress("160 John St, Seattle, WA 98109")[0]["coordinates"]
The_Downtown_School_A_Lakeside_School = (47.61977, -122.35337)
print(The_Downtown_School_A_Lakeside_School)
inputFile = filedialog.askopenfilename(filetypes = (("Comma Seperated Values","*.csv"),("All files", "*.*")))

with open(inputFile, newline = "") as file :
    inputDataRaw = [row for row in csv.reader(file)]

total = len(inputDataRaw)
print("Grabbed file with " + str(total) + " colleges.\n")
print("1: Use U.S Census")
print("2: Provide lat/long file")
choice = input(":")

NUMBER_OF_ROWS = 1000

if choice == "1" :
    receiveData = []
    top = math.ceil(len(inputDataRaw)/NUMBER_OF_ROWS)
    for send in range(top) :
        if send == top - 1 :
            end = len(inputDataRaw) - 1
        else :
            end = (send + 1) * NUMBER_OF_ROWS
        with open("tempSend.csv", "w", newline = "") as file:
            csv_writer = csv.writer(file, dialect='excel')
            for index, row in enumerate(inputDataRaw[send*NUMBER_OF_ROWS:end]) :
                if row[2] == "Institution" :
                    try:
                        temp = row[1].split(", ")
                        if len(temp) > 3 :
                            temp2 = "\""
                            for i in range(len(temp) - 2) :
                                temp2 += " " + temp[i]
                            temp2 += "\""
                            temp = [temp2, temp[-2], temp[-1]]
                        temp[2] = temp[2].split(" ")
                        if len(temp[2]) == 1 :
                            temp[2].append("-")
                        toWrite = [row[0], temp[0], temp[1], temp[2][0], temp[2][1]]
                        print(toWrite)
                        csv_writer.writerow(toWrite)
                    except Exception as e:
                        pass
            file.close()
        print(str(send) + " out of " + str(top) + ". Getting Data...\n")
        currentBatch = cg.addressbatch("tempSend.csv")
        receiveData += currentBatch
        sleep(1)
        os.remove("tempSend.csv")
        sleep(5)
        print("Done!\n")
        with open("OutReceive.csv", "a", newline = "") as file :  
            csv_writer = csv.writer(file, dialect='excel')
            csv_writer.writerows(currentBatch)

if choice == "2" :
    inputFile = filedialog.askopenfilename(filetypes = (("Comma Seperated Values","*.csv"),("All files", "*.*")))
    
    with open(inputFile, newline = "") as file :
        receiveData = [eval(row) for row in csv.reader(file)]
    
totalDone = 0
total = len(receiveData)
print(receiveData)
with open("OutputDistances.csv", "w", newline = "") as file :  
    csv_writer = csv.writer(file, dialect='excel')
    csv_writer.writerow(["School", "Address", "Lat/Lon", "Distance (Miles)"])
    for index, school in enumerate(receiveData) :    
        
        collegeLocation = (school["lat"], school["lon"])

        if collegeLocation[0] != None :
            distance = getDistance(The_Downtown_School_A_Lakeside_School, collegeLocation)

            print(str(index) + " out of " + str(total) + "\nLocation: " + school["id"] + "\nDistance: " + str(distance))
            
            csv_writer.writerow([school["id"], school["address"], collegeLocation, distance])
        print("Total done: " + str(index) + "\n")

    file.close()
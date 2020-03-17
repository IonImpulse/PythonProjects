import math
import tkinter as tk
from tkinter import filedialog
import csv

def getDistanceReal(origin, destination):
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
    distance_in_feet : float

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
    d = radius * c * 0.6213712 * 5280

    return d

def getDistanceBad(origin, destination) :
    lat1, lon1 = origin
    lat2, lon2 = destination

    d = math.sqrt(((lat2-lat1)**2) + ((lon2-lon1)**2))

    return d

def angleFromCoordinateGood(lat1, long1, lat2, long2):
    dLon = (long2 - long1)

    y = math.sin(dLon) * math.cos(lat2)
    x = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(dLon)

    brng = math.atan2(y, x)

    brng = math.degrees(brng)
    brng = (brng + 360) % 360
    brng = 360 - brng # count degrees clockwise - remove to make counter-clockwise

    return brng

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

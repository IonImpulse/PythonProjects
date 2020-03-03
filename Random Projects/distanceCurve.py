import math
import tkinter as tk
from tkinter import filedialog
import csv

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

root = tk.Tk()
root.withdraw()

inputFile = filedialog.askopenfilename(filetypes = (("Comma Seperated Values","*.csv"),("All files", "*.*")))

with open(inputFile, newline = "") as file :
    inputDataRaw = [row for row in csv.reader(file)]

total = 0

for i in range(len(inputDataRaw) - 1) :
    total += getDistance((float(inputDataRaw[i][0]),float(inputDataRaw[i][1])), (float(inputDataRaw[i + 1][0]), float(inputDataRaw[i + 1][1])))
    print(total)
import censusgeocode as cg
import csv
import tkinter as tk
from tkinter import filedialog
from time import sleep
import math
import os

root = tk.Tk()
root.withdraw()

#Main class to act as object for program
class geo_mean_finder :
    #Initialization
    def __init__(self) :
        
        #Open dialog box to ask for file in csv format
        #NOTE: Must have a header of [first name, last name, birthdate, address]
        inputFile = filedialog.askopenfilename(filetypes = (("Comma Seperated Values","*.csv"),("All files", "*.*")))

        #Open file and read
        with open(inputFile, newline = "") as file :
            self.inputDataRaw = [row for row in csv.reader(file)]

        #Delete header
        del self.inputDataRaw[0]

        #Output number of addresses
        total = len(self.inputDataRaw)
        print("Grabbed file with " + str(total) + " addresses.\n")
        
    #API request phase
    def get_census_data(self, debug = False) :
        
        #Create list to store return data
        self.receiveData = []

        #Store list of people in firstname lastname format
        self.people_list = [i[0] + " " + i[1] for i in self.inputDataRaw]
        
        #Create and write to temporary sending csv file
        with open("tempSend.csv", "w", newline = "\n") as file:
            csv_writer = csv.writer(file, dialect='excel')

            #Loop over the input data
            for index, row in enumerate(self.inputDataRaw) :
                
                #Split address into streetname, city, state, zip code
                temp = row[3].split(",")

                #Create list in proper format for the census API
                toWrite = [self.people_list[index], temp[0], temp[1], temp[2], temp[3]]
                print(toWrite)
                
                #Write row
                csv_writer.writerow(toWrite)
        
        #Send API request
        self.receiveData = cg.addressbatch("tempSend.csv")        
        
        if debug == True :
            for house in self.receiveData :
                print(house)

        print("Done!\n")

    def get_mean_location(self) :
        #Convert all to cartesian (x,y,z) coordinates
        coords = []
        total_weight = len(self.receiveData)
        
        for index, house in enumerate(self.receiveData) :
            #Wrap in try/catch incase did not return a valid lat/lon
            try :
                #Get lat and lon
                temp_lat = house["lat"] * (math.pi/180)
                temp_lon = house["lon"] * (math.pi/180)
                
                #Convert to cartesian coords
                x = math.cos(temp_lat) * math.cos(temp_lon)
                y = math.cos(temp_lat) * math.sin(temp_lon)
                z = math.sin(temp_lat)

                coords.append((x, y, z))
        
            except Exception as e :
                print("Skipping " + house["id"] + ", trying to use zip code as approximate lat/lon...")

            
        #Get combined average, divided by weight
        avg_x = sum([i[0] for i in coords])/total_weight
        avg_y = sum([i[1] for i in coords])/total_weight
        avg_z = sum([i[2] for i in coords])/total_weight

        #Lon, Lat
        hyp = math.sqrt(avg_x * avg_x + avg_y * avg_y)
        lon = math.atan2(avg_y, avg_x) * (180/math.pi)
        lat = math.atan2(avg_z, hyp) * (180/math.pi)
        
        midpoint = (lat, lon)
        mid_address = cg.coordinates(lon, lat)
        sleep(1)
        return midpoint, mid_address


#Main sequence
finder = geo_mean_finder()
finder.get_census_data(debug=False)
midpoint, mid_address = finder.get_mean_location()
print(midpoint)
print(mid_address)
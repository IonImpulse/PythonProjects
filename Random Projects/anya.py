from geopy.distance import geodesic
from geopy.geocoders import Nominatim
import csv

geolocator = Nominatim(user_agent="edv121@outlook.com")

location = geolocator.geocode("160 John St, Seattle, WA 98109")
The_Downtown_School_A_Lakeside_School = (location.latitude, location.longitude)
print("location")
with open("C:\\Users\\ionim\\Documents\\GitHub\\PythonProjects\\Random Projects\\InstitutionCampus.csv", newline = "") as file :
    inputDataRaw = [row for row in csv.reader(file)]

total = len(inputDataRaw)
outputTable = [["Name","Address","Distance from DTS"]]

for index, school in enumerate(inputDataRaw) :
    if school[2] == "Institution" :
        location = geolocator.geocode(school[1])
        if location != None :
            location = (location.latitude, location.longitude)
            distance = geodesic(The_Downtown_School_A_Lakeside_School, location).miles
            print(str(index) + "out of " + str(total) + "\nLocation: " + school[0] + "\nDistance: " + str(distance))
            print("")
            outputTable.append([school[0], school[1], distance])
        else :
            print("Skipping " + school[0])
            print("")

with open("C:\\Users\\ionim\\Documents\\GitHub\\PythonProjects\\Random Projects\\OutputDistances.csv", "w", newline = "") as file :
    csv_writer = csv.writer(file, dialect='excel')
    for i in outputTable:
        csv_writer.writerow(i)
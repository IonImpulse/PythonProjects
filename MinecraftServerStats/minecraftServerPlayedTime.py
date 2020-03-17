import gzip
import csv
import tkinter as tk
from tkinter import filedialog
from time import sleep
import os
import sys
import math

class player() :
    def __init__(self, name, uuid) :
        self.name = name
        self.uuid = uuid
        self.ipList = []
        self.connectDisconnect = []
        self.computedSeconds = False
        self.numOfMessages = 0

    def addIP(self, ip) :
        if ip not in self.ipList :
            self.ipList.append(ip)

    def addConnectDisconnect(self, time) :
        self.connectDisconnect.append(time)
    
    def addNumOfMessages(self) :
        self.numOfMessages += 1

    def computeTime(self) :
        seconds = 0
        logins = int(math.floor(len(self.connectDisconnect)/2))

        for timeIndex in range(logins)  :
            diffH = int(self.connectDisconnect[(timeIndex * 2) + 1][0]) - int(self.connectDisconnect[timeIndex * 2][0])
            if abs(diffH) != diffH :
                #assume nobody is on for more then 24h, no way to tell also
                diffH += 24
            
            seconds += diffH * 60 * 60

            diffM = int(self.connectDisconnect[(timeIndex * 2) + 1][1]) - int(self.connectDisconnect[timeIndex * 2][1])

            seconds += diffM * 60

            diffS = int(self.connectDisconnect[(timeIndex * 2) + 1][2]) - int(self.connectDisconnect[timeIndex * 2][2])

            seconds += diffS

        self.computedSeconds = seconds

        return seconds
    
    def readTime(self) :
        m, s = divmod(self.computedSeconds, 60)
        h, m = divmod(m, 60)

        return h, m, s


class playerTimer :
    def __init__(self) :
        clear = lambda: os.system('cls')        
        user = os.environ.get('USERNAME')

    
    def getFiles() :
        inputDir = filedialog.askdirectory()
        filesList = os.listdir(inputDir)
        allLogs = []

        for fileName in filesList :
            if fileName [-2:] == "gz" :
                tempFilePath = inputDir + "\\" + fileName
                try :
                    f = gzip.open(tempFilePath, 'rb')
                    allLogs.append(f.readlines())
                    f.close()
                except Exception as e :
                    print("Could not open " + fileName + ". Error: " + str(e))
        
        return allLogs

    def readFiles(textFiles) :
        def getTime(line) :
            time = tuple(str(line)[3:11].split(":"))
            return time

        playerList = {}
        for log in textFiles :
            for line in log :
                tempLine = str(line).split(" ")

                if len(tempLine) > 4 :
                    if tempLine[1] == "[User" :
                        if tempLine[7] not in playerList :
                            playerList[tempLine[7]] = player(tempLine[7], tempLine[9][:-5])

                    elif tempLine[4] == "logged" :
                        name = tempLine[3].split("[")[0]
                        ip = tempLine[3].split("[/")[1][:-1]

                        playerList[name].addIP(ip)
                        playerList[name].addConnectDisconnect(getTime(line))

                    elif tempLine[4] == "left" :
                        name = tempLine[3]
                        
                        playerList[name].addConnectDisconnect(getTime(line))
                    
                    elif tempLine[2] == "Chat" :
                        name = tempLine[6][1:-1]
                        if name == playerList[name].name :
                            playerList[name].addNumOfMessages()
        
        return playerList

root = tk.Tk()
root.withdraw()

logs = playerTimer.getFiles()
playerList = playerTimer.readFiles(logs)
outputArray = [["Name", "Time (Seconds)", "Time (H:M:S)", "Messages Sent"]]
for person in playerList :
    playerList[person].computeTime()
    hours, minutes, seconds = playerList[person].readTime()
    print(playerList[person].name + " was UUID " + playerList[person].uuid)
    print("They have spent " + str(hours) + " hours, " + str(minutes) + " minutes, and " + str(seconds) + " seconds on the server.")
    print("They have also sent " + str(playerList[person].numOfMessages) + " messages in chat.")
    print("IPs used: ")
    for ip in playerList[person].ipList :
        print(ip)
    print("---------------------------------------")

    outputArray.append([playerList[person].name, playerList[person].computedSeconds, str(hours) + ":" + str(minutes) + ":" + str(seconds),playerList[person].numOfMessages])

outputArray[1:] = sorted(outputArray[1:],key=lambda row: int(row[1]), reverse=True)

with open("outputLog.csv", "w", newline='') as target :
    csv_writer = csv.writer(target, dialect='excel')
    csv_writer.writerows(outputArray)
import math
import itertools
exit = False

#Test
#P1:
#R(t), R(T); U, u
#P2:
#R(T), R(T); u, u
def createSquareArray(arr1, arr2) :
    outputArr = []
    for i in arr2 :
        outputArr.append([j for j in arr1])
    for index, i in enumerate(arr2) :
        for index2, j in enumerate(arr1) :
            outputArr[index][index2] = str(outputArr[index][index2]) + str(i)
    
    return outputArr

def outputSquare(par1, par2) :
    maximum = max(par1, key=len)
    if max(par2, key=len) > maximum :
        maximum = max(par2, key=len)
    
    maximum = len(maximum) * 2

    square = createSquareArray(parent1, parent2)
    
    outputArr = []

    tempString = " " * maximum + "|"

    for j in par1 :
            tempMax = maximum - len(j)
            tempString += j + (" " * tempMax) + "|"

    outputArr.append(tempString)

    for index, item in enumerate(square) :
        outputArr.append(str("-" * ((maximum + 1) * (len(par1) + 1))))
        tempString = ""
        tempMax = maximum - len(par2[index])

        tempString += par2[index] + (" " * tempMax) + "|"

        for i in item :
            tempMax = maximum - len(i)
            tempString += i + (" " * tempMax) + "|"
        
        outputArr.append(tempString)

    outputArr.append(str("-" * ((maximum + 1) * (len(par1) + 1))))
    print("\n")
    for i in outputArr :
        print(i)
    
while exit == False :
    print("Enter Parent 1's Gene(s):")
    parent1In = input(":").replace(" ", "").split(";")
    parent1 = []
    for index in range(len(parent1In[0])) :
        tempPerm = intertools.permutations([i for i in parent1In])
        

    print("Enter Parent 2's Gene(s):")
    parent2In = input(":").replace(" ", "").split(",")
      
    outputSquare(parent1, parent2)
    print("\nPress enter to restart")
    input(":")
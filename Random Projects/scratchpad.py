from math import *
hello = [0,0,0,0,0]
def iterate(intList, top) :
    endList = []
    for h in range(len(intList)) :
        endList.append(top)
    while intList != endList :
        iter = False
        j = len(intList)-1
        while iter == False and j >= 0:
            if intList[j] == top :
                for l in range(len(intList)-j) :
                    intList[l + j] = 0
            else :
                intList[j] = intList[j] + 1
                iter = True
            j = j - 1
        print(intList)
iterate(hello,5)

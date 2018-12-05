from math import *
from random import *
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
def parser(input,output):
    j = -1
    for i in input :
        j = j + 1
        if i == "_" :
            output.append("_")
            output.append("(")
        elif i == "+" :
            output.append(")")
            output.append("+")
        elif i == "(" :
            output.append("(")
            #parser(input[i:input.index(")",j)],parsed)
        elif i == ")" :
            output.append(")")
        elif i == "=" :
            output.append(")")
            output.append("=")
        elif is_number(i) == True :
            output.append(i)
        elif i.isupper() == True :
            output.append(i)
        elif i.isupper() == False :
            output[len(output)-1] = output[len(output)-1]+i
    output.append(")")
def indexer(input,output) :
    output.append(" ")
    for i in input :
        if i != "_" and i != "+" and i != "(" and i != ")" and i != "=" and is_number(i) == False :
            e = 0
            for j in output :
                if j == i :
                    e = 1
            if e == 0 :
                output.append(i)
    output.remove(" ")
def iterate(intList, top) :
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
def solve(input,indexList,output) :
    spots = 0
    temp = ""
    for j in range(spots) :
        temp = temp + "0"
    o = ""
    equ1 = []
    equ2 = []
    l = -1
    while o != "=" :
        l = l + 1
        o = input[0]
        equ1.append(o)
        del input[0]
    for o in input :
        equ2.append(o)
    equ1.remove("=")
    print(equ1)
    print(equ2)
    spots1 = []
    spots2 = []
    for word in range(len(equ1)) :
        if equ1[word] == "_" :
            spots1.append(word)
    for word in range(len(equ2)) :
        if equ2[word] == "_" :
            spots2.append(word)
    tally = [[],[]]
    for items in indexList :
        tally[0].append(0)
        tally[1].append(0)
    blank = tally
    for o in temp :
        output.append(int(o))
    solved = False
    tester = []
    for j in range(len(spots1)+len(spots2)) :
        tester.append(1)
    topN = 1
    while solved == False :
        topN = topN + 1
        endList = []
        for h in range(len(tester)) :
            endList.append(topN)
        while tester != endList and solved == False :
            tally = blank
            iterate(tester,topN)
            y = 0
            for i in spots1 :
                y = y + 1
                for element in range(len(indexList)) :
                    if equ1[i+element] == indexList[element] and equ1[i+element] != "_":
                        if is_number(equ1[i+element+1]) == True :
                            tally[0][element] = tally[0][element] + (int(equ1[i+element+1]) * tester[y])
                        else :
                            tally[0][element] = tally[0][element] + tester[y]
            for i in spots2 :
                for element in range(len(indexList)) :
                    if equ2[i+element] == indexList[element] and equ2[i+element] != "_":
                        if is_number(equ2[i+element+1]) == True :
                            tally[1][element] = tally[1][element] + (int(equ2[y+element+1]) * tester[y+len(spots1)])
                        else :
                            tally[1][element] = tally[1][element] + tester[i+len(spots1)]
            print(tester)
            print(tally)
            if tally[0] == tally[1] :
                solved = True
                print(tester)
                print(tally)
print("Welcome to Chemistry Balancer!")
print("==============================")
print("Input Equation:")
#_NaBr+_Cl2=_NaCl+_Br2
#_Ch4+_O2=_CO2+_H2O
inputE = str(input(":"))
parsed = []
indexL = []
result = []
parser(inputE,parsed)
indexer(parsed,indexL)
print(parsed)
print(indexL)
solve(parsed,indexL,result)
print(result)

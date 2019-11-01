#For operations, use +,-,*, and / before to indicate operations. Ex: *3
#For putting numbers on the end, just put the number. Ex: 3
#Reverse is >, and backspace is <
#Change number is number-number
from math import *
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
ts = []
ops = []
print("Welcome to CalcGameSolver!")
print("Start?")
ts.append(float(input(":")))
print("End?")
ts.append(float(input(":")))
print("Moves?")
ts.append(int(input(":")))
print("Number of Operations?")
ts.append(int(input(":")))
for i in range(ts[3]) :
    print("Operation #"+str(i+1))
    ops.append(str(input(":")))
print("==Solving==")
s = ts[0]
e = ts[1]
o = []
endList = []
for i in range(ts[2]) :
    o.append(0)
    endList.append(ts[3]-1)

solved = False
numberOfSolves = 0
while solved == False :
    if endList == o :
        print("No Solution")
        break
    s = ts[0]
    tempList = [s]
    for j in range(ts[2]) :
        if str(ops[o[j]])[:1] == "*" :
            s = float(str(ops[o[j]])[1:]) * s
        elif str(ops[o[j]])[:1] == "/" :
            s = s / float(str(ops[o[j]])[1:])
        elif str(ops[o[j]])[:1] == "+" :
            s = float(str(ops[o[j]])[1:]) + s
        elif str(ops[o[j]])[:1] == "-" :
            s = s - float(str(ops[o[j]])[1:])
        elif str(ops[o[j]])[:1] == "^" :
            s = s ** float(str(ops[o[j]])[1:])
        elif len(str(ops[o[j]])) > 1 :
            if ">" in str(ops[o[j]]) :
                pos = str(ops[o[j]]).index(">")
                start = int(str(ops[o[j]])[:pos])
                end = int(str(ops[o[j]])[pos + 1:])
                number = ""
                for i in str(s) :
                    if i == str(start) :
                        number += str(end)
                    else :
                        number += str(i)
            s = float(number)
        elif str(ops[o[j]])[:1]== ">" :
            if s < 0 :
                s = -(float(str(int(round(-s,0)))[::-1]))
            else :
                s = float(str(int(round(s,0)))[::-1])
        elif str(ops[o[j]])[:1] == "<" :
            if s < 10 and s > -10 :
                s = 0
            else :
                s = float(str(int(round(s,0)))[:-1])
        else :
            s = float(str(int(round(s,0)))+str(ops[o[j]]))
        tempList.append(s)
    if round(s,5) == round(e,5) :
        numberOfSolves += 1
        print("Solve # " + str(numberOfSolves))
        for index, i in enumerate(o) :
            print(ops[i], tempList[index + 1])
        print("Continue? Y/n")
        choice = input(":")
        if choice.lower() == "n" :
            solved = True
    iterate(o,ts[3]-1)
input()

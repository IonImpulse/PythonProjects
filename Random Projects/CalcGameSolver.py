#For operations, use +,-,*, and / before to indicate operations. Ex: *3
#For putting numbers on the end, just put the number. Ex: 3
#Reverse is >, and backspace is <
from math import *
from random import *
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
    endList.append(ts[3])
while round(s,5) != round(e,5) :
    if endList == o :
        print("No Solution")
        break
    s = ts[0]
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
    if round(s,5) == round(e,5) :
        for i in o :
            print(ops[i])
    iterate(o,ts[3]-1)

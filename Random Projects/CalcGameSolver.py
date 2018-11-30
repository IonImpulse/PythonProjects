from math import *
from random import *
ts = []
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
    ts.append(str(input(":")))
print("==Solving==")
s = ts[0]
e = ts[1]
while round(s,5) != round(e,5) :
    o = []
    s = ts[0]
    for j in range(ts[2]) :
        o.append(ts[randint(3,len(ts)-1)])
        if str(o[j])[:1] == "*" :
            s = float(str(o[j])[1:]) * s
        elif str(o[j])[:1] == "/" :
            s = s / float(str(o[j])[1:])
        elif str(o[j])[:1] == "+" :
            s = float(str(o[j])[1:]) + s
        elif str(o[j])[:1] == "-" :
            s = s - float(str(o[j])[1:])
        elif str(o[j])[:1] == "^" :
            s = s ** float(str(o[j])[1:])
        elif str(o[j])[:1] == ">" :
            if s < 0 :
                s = -(float(str(int(round(-s,0)))[::-1]))
            else :
                s = float(str(int(round(s,0)))[::-1])
        elif str(o[j])[:1] == "<" :
            if s < 10 and s > -10 :
                s = 0
            else :
                s = float(str(int(round(s,0)))[:-1])
        else :
            s = float(str(s)+str(o[j])[:1])
print(o)

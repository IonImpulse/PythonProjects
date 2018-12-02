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
    spots1 = 0
    spots2 = 0
    for word in equ1 :
        if word == "_" :
            spots1 = spots1 + 1
    for word in equ1 :
        if word == "_" :
            spots2 = spots2 + 1
    tally = [[],[]]
    for items in indexList :
        tally[0].append(0)
        tally[1].append(0)
    for o in temp :
        output.append(int(o))
    solved = False
    while solved == False :
        p = 0
        for i in range(spots1-1) :
            p = p + 1
            temp = equ1[p:equ1.index("+")]
            solved = True
            p = p + len(temp)
            print(temp)
        
print("Welcome to Chemistry Balancer!")
print("==============================")
print("Input Equation:")
#_NaBr+_Cl2=_NaCl+_Br2
inputE = str(input(":"))
parsed = []
indexL = []
result = []
parser(inputE,parsed)
indexer(parsed,indexL)
print(parsed)
print(indexL)
solve(parsed,indexL,result)

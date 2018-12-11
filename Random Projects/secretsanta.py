#Chad, Anon, Stacy, Fred, Karen, George, Brian
from random import *
from time import *
import os
clear = lambda: os.system('cls')
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
def scrambled(orig):
    dest = orig[:]
    shuffle(dest)
    return dest
print("Enter list of names, seperated by commas:")
names = str(input(":"))
names = names.replace(" ","")
namesList = names.split(",")
e = False
while e == False :
    namesListS = scrambled(namesList)
    e = True
    for i in range(len(namesList)) :
        if namesList[i] == namesListS[i] :
            e = False
clear()
choice = ""
while True :
    clear()
    print("==Enter Number==")
    x = 0
    for i in namesList :
        x = x + 1
        print(str(x)+": "+str(i))
    choice = str(input(":"))
    if is_number(choice) :
        try :
            print(namesListS[int(choice)-1])
            sleep(5)
        except IndexError:
            print("Out of range!")
            sleep(1)
    if choice == "exit" or choice == "Exit" :
        break

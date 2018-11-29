from math import *
schedule = {}
calendar = [
    ["01","02","03","04","05","06","07"],
    ["08","09","10","11","12","13","14"],
    ["15","16","17","18","19","20","21"],
    ["22","23","24","25","26","27","28"],
    ["29","30","31","--","--","--","--"],
    ]
def display():
    print("====================================")
    for i in range(5) :
        output = "|"
        for o in range(7) :
            e = False
            for item in schedule :
                if (i*7) + o + 1 == schedule[item] :
                    e = True
            if e == True :
                output = output + "=" + calendar[i][o] + "=|"
            else :
                output = output + " " + calendar[i][o] + " |"
        print(output)
        print("====================================")
print("==Welcome to your Virtual Calendar!==\n")
while True :
    print("==Main Menu==")
    print("1: View")
    print("2: Add/Edit")
    print("3: Remove")
    print("4: Main Menu")
    print("5: Exit")
    choice = int(input(":"))
    if choice == 1 :
        display()
        print("Day?")
        choice1 = int(input(":"))
        for item in schedule :
            if schedule[item] == choice1 :
                print(item)
    if choice == 2 :
        print("Name?")
        temp = str(input(":"))
        print("Day?")
        schedule[temp] = int(input(":"))
    if choice == 3 :
        print("Name?")
        del schedule[str(input(":"))]
    if choice == 5 :
        print("==Exiting==")
        break

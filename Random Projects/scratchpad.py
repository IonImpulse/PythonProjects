import time
name = input("Name: ")
print("Hello there " + name + "!")
print("How are you feeling?\n")
print("1: Good")
print("2: Normal")
print("3: Bad")
feeling = int(input("\nChoice: "))
if feeling == 1 :
    print("That's great!")
if feeling == 2 :
    print("Hope you have a good day!")
if feeling == 3 :
    print("I hope you feel better soon!")
print("\nWhat year were you born in?")
year = int(input(":"))
year = int(time.strftime("%Y")) - year
print("You are " + str(year) + " years old!")

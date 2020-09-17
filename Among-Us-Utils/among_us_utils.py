import os
import time

def clear_term() :
    os.system('cls' if os.name == 'nt' else 'clear')

def calculate_odds(people) :
    return

def print_vouch_dict(vouch_pairs) :
    

people = []
with open("people.txt", "r") as f :
    people = f.readline().replace(" ", "").split(",")

# Removal loop
keep_removing = True

while keep_removing :
    clear_term()
    print("===== Setup =====\n")
    print("Remove people by typing their number. To exit, make no choice.\n")
    for index, i in enumerate(people) :
        print(f"{index + 1}: {i}")

    choice = input(":")

    if choice == "" :
        keep_removing = False
    else :
        try:
            choice = int(choice)

            print(f"Removed {people[choice - 1]}")
            time.sleep(.2)
            del people[choice - 1]

        except Exception as e :
            print("Please enter a valid number")
            


clear_term()
print("Final people list:")
print(people)
time.sleep(.5)
clear_term()

# Game loop
game = True

while game :
    clear_term()
    print("===== Game Mode =====\n")
    print_vouch_dict("")


vouch_pairs = {}

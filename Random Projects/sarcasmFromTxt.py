file = input("Enter full file name: ")
file = open(file, "r")
lists = list(file.read())
loopIndex = 0
for x, y in enumerate(lists) :
    if y != " " :
        if loopIndex % 2 == 0 :
            lists[x] = y.upper()
        else :
            lists[x] = y.lower()
        loopIndex += 1
print("".join(lists))
saveName = input("Enter save name: ")
file = open(saveName, "w")
file.write("".join(lists))

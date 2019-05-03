file = input("Enter full file name: ")
file = open(file, "r")
lists = list(file.read())
for x, y in enumerate(lists) :
    if x % 2 == 0 :
        lists[x] = y.upper()
    else :
        lists[x] = y.lower()
print("".join(lists))
saveName = input("Enter save name: ")
file = open(saveName, "w")
file.write("".join(lists))

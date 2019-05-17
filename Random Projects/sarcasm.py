sentence = ""
print("Type in sentence, \"exit\" to close: ")
while sentence.lower() != "exit" :
    sentence = input(":")
    lists = list(sentence)
    loopIndex = 0
    for x, y in enumerate(lists) :
        if y != " " :
            if loopIndex % 2 == 0 :
                lists[x] = y.upper()
            else :
                lists[x] = y.lower()
            loopIndex += 1
    print("".join(lists))

import random
sentence = ""
while sentence.lower() != "exit" :
    sentence = input("Type in sentence, \"exit\" to close: ")
    lists = list(sentence)
    for x, y in enumerate(lists) :
        if x % 2 == 0 :
            lists[x] = y.upper()
        else :
            lists[x] = y.lower()
    print("".join(lists))

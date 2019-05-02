import random
sentence = input("Type in sentence: ")
lists = list(sentence)
for x, y in enumerate(lists) :
    if x % 2 == 0 :
        lists[x] = lists[x].upper()
    else :
        lists[x] = lists[x].lower()
print("".join(lists))

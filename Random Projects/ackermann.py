import sys
sys.setrecursionlimit(10000)
def naive_ackermann(m, n):
    if m == 0:
        return n + 1
    elif n == 0:
        return naive_ackermann(m - 1, 1)
    else:
        return naive_ackermann(m - 1, naive_ackermann(m, n - 1))
def iterate(intList, top) :
    iter = False
    j = len(intList)-1
    while iter == False and j >= 0:
        if intList[j] == top :
            for l in range(len(intList)-j) :
                intList[l + j] = 0
        else :
            intList[j] = intList[j] + 1
            iter = True
        j = j - 1
i = 1
items = [1,1]
while True :
    print(items)
    print(naive_ackermann(items[0], items[1]))
    if all(item == i for item in items) == True :
        i = i + 1
    iterate(items, i)

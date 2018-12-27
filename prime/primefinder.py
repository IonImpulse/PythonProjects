from math import *
n = int(input(":"))
i = 3
l = [3]
k = 0
while i < n :
    i = i + 2
    u = 0
    e = 0
    m = sqrt(i)
    while e == 0 and u < k and l[u]<m:
        if i%(l[u]) == 0 :
            e = 1
        u = u+1
    if e == 0 :
      l.append(i)
      k = k + 1
print(l)
print("Save? Y/n")
choice = input(":")
if choice == "Y" :
    with open('primes.txt', 'w') as f:
        for item in l:
            f.write("%s," % item)

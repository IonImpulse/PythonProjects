import math
exit = False

while exit == False :
    print("Sex based?")
    print("1: Yes")
    print("2: No")
    choice = input(":")
    if choice == "1" :
        pass
    elif choice == "2" :
        print("\nHow many genes per parent?")
        genesPerP = int(input(":"))
        geneList = []

        for j in range(genesPerP) :
            print("\nHow many alleles in gene #{0}?".format(j+1))
            numOfAlleles = int(input(":"))
            
            geneList.append([])    

            for i in range(numOfAlleles) :
                print("Allele #{0}".format(i+1))
                geneList[j].append(input(":"))
        
        print("\nParent #1:")
        parent1 = []

        for i in range(genesPerP) :
            print("Select allele:")
            for j, item in enumerate(geneList[i]) :
                print("{0}: {1}".format(j + 1, geneList[i][j]))
            parent1.append(geneList[i][int(input(":")) - 1])
        
        print("\nParent #2:")
        parent2 = []

        for i in range(genesPerP) :
            print("Select allele:")
            for j, item in enumerate(geneList[i]) :
                print("{0}: {1}".format(j + 1, geneList[i][j]))
            parent1.append(geneList[i][int(input(":")) - 1])

        print(parent1)
        print(parent2)
    else :
        print("Invalid input")
        input()
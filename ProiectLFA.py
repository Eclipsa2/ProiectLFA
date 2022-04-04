fisier = open("input.txt", "r")
n = fisier.readline()
adiacenta = [[] for _ in range(int(n))]
m = fisier.readline()
drum = []

for i in range(int(m)):
    input = fisier.readline()
    inputSplit = input.split()
    adiacenta[int(inputSplit[0])].append((int(inputSplit[1]), inputSplit[2]))

#print(adiacenta)

def dfs(nod, cuvant, indexCuvant):
    global adiacenta, drum, stariFinaleInt

    drum.append(nod)

    if indexCuvant == len(cuvant):
        if nod in stariFinaleInt:
            return True
        else:
            return False

    for i in adiacenta[nod]:
        if cuvant[indexCuvant] == i[1]:
            final = dfs(i[0], cuvant, indexCuvant + 1)
            if (final == True):
                return True
            drum.pop()

    return False

stareInitiala = int(fisier.readline())
stariFinale = fisier.readline()
stariFinaleSplit = stariFinale.split()
stariFinaleInt = []
for i in range(int(stariFinaleSplit[0])):
    stariFinaleInt.append(int(stariFinaleSplit[i+1]))
nrCuvinte = int(fisier.readline())

for i in range(nrCuvinte):
    cuvant = fisier.readline()
    if(dfs(stareInitiala, cuvant[:-1], 0)):
        print("DA")
        print(drum)
    else:
        print("NU")
    drum = []

#if (dfs(0, "ab", 0, 5)):
    #print("DA")
    #print(drum)
#else:
    #print("NU")
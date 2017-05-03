import math
translator = {}

def allPermutations(Set): #Generates all permutations of Set
    n = len(Set)
    maxPerms = math.factorial(n)
    Sub = substitute(Set)
    for i in range(maxPerms):
        Ori = reSub(Sub)
        print(Ori,i)
        algorithm1(Sub)
    translator = {}

def allSubsetsInRange(Set,Min,Max): #Generates all subsets of length Min to length Max of Set.
    Max = Max + 1                   #if only r combinations are wanted use r = Min = Max.
    subtitute = substitute(Set)
    counter = 1
    for i in range(Min,Max):
        subset = firstX(i,subtitute)
        MaxCs = binomial(len(Set),i)
        for c in range(MaxCs):
            ori = reSub(subset)
            print(ori, counter)
            counter += 1
            algorithm3(subtitute,subset)
    translator = {}

def allBitstrings(n): #Generates all bitstring of length n
    String = []
    for i in range(n):
        String.append(0)
    Max = 2 ** n
    for i in range(Max):
        print(String)
        algorithm2(String)

def algorithm1(List): #Generate next permutation in lexicographic order.
    n = len(List)-1
    j = n-1
    while List[j] > List[j+1]:
        j = j - 1
    k = n
    while List[j] > List[k]:
        k = k - 1
    temp = List[j]
    List[j] = List[k]
    List[k] = temp
    r = n
    s = j + 1
    while r > s:
        temp = List[r]
        List[r] = List[s]
        List[s] = temp
        r = r - 1
        s = s + 1
    return List

def algorithm2(BitString): #Generate the next larger bit string.
    i = len(BitString) - 1
    while (BitString[i] == 1) & (i > 0):
        BitString[i] = 0
        i = i - 1
    BitString[i] = 1
    return BitString

def algorithm3(List,After): #Generate the next r-Combination after After in lexicographic order.
    r = len(After)-1
    i = r
    while After[i] == List[len(List)-1] - r + i:
        i = i - 1
    After[i] = After[i] + 1
    for j in range (i+1,r+1):
        After[j] = After[i] + (j-i)

def substitute(List): #substitutes members of a list with numbers 1 - len(list). For use with algorithm3.
    i = 1
    Sub = []
    for entry in List:
        translator[i] = entry
        Sub.append(i)
        i = i + 1        
    return Sub

def reSub(List): #back substitutes the List previously replaced with numbers.
    Original = []
    for entry in List:
        Original.append(translator[entry])
    return Original

def firstX(X,Set): #Gets the first X members of Set.
    subset = []
    for i in range(X):
        subset.append(Set[i])
    return subset

def binomial(n,r): #Calculates the binomial of (n,r).
    bi = (math.factorial(n) / (math.factorial(r) * math.factorial(n - r)))
    return int(bi)

def disjointSet(n,union):
    array = list(range(n+1))

    for i,j in union:
        if array[i] == array[j]:
            continue
        else:
            array[j] = min(i,j)
            
    return array

def checkConnectivity(disjointSetValues,toCheck):
    for i,j in toCheck:
        firstCheck = disjointSetValues[i]
        secondCheck = disjointSetValues[j]
        while i != firstCheck:
            i = firstCheck
            firstCheck = disjointSetValues[firstCheck]

        while j != secondCheck:
            j = secondCheck
            secondCheck = disjointSetValues[secondCheck]

        if secondCheck == firstCheck:
            print(True)
        else:
            print(False)


if __name__ == '__main__':
    n = 9
    union = [(0,1),(0,2),(1,3),(4,8),(5,6),(5,7)]

    checkConnectivity(disjointSet(n,union),[(0,3),(1,5),(7,8)])
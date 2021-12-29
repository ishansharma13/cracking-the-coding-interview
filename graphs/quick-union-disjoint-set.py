"""
(x,y) => x is the node where y is to be joined

we find the root node of x, replace the value of y with root of x, but do not replace the values where y acts as the root node


"""


def disjointSet(n, union):
    array = list(range(n+1))

    for i, j in union:
        if array[i] == array[j]:
            continue
        else:
            array[j] = array[array[i]]

    return array


def checkConnectivity(disjointSetValues, toCheck):
    for i, j in toCheck:
        firstCheck = find(array,i)
        secondCheck = find(array,j)

        if secondCheck == firstCheck:
            print(True)
        else:
            print(False)

def find(array,x):
    i = x
    firstCheck = array[x]
    while x != firstCheck:
            x = firstCheck
            firstCheck = array[firstCheck]
    """ Responsible for path compression, as for each find it stores the root value at i(intial x value) which reduces the subsequent searches"""
    array[i] = firstCheck
    return firstCheck
if __name__ == '__main__':
    n = 10
    union = [(1, 2), (2, 5), (5, 6), (6, 7),(3,8),(8,9),(9,4)]
    array = disjointSet(n, union)
    toCheck = [(1,5),(5,7),(4,9)]
    checkConnectivity(disjointSet(n, union), toCheck)

"""
when two nodes are to be connected, then each element here stores the root value in the array,
x,y =>
find root node of x, replace the value of y as well as the children of y with rootX
"""


def disjointSet(n, union):
    array = list(range(n+1))

    for i, j in union:
        if array[i] != array[j]:
            for k in range(len(array)):
                if array[k] == array[j]:
                    array[k] = array[i]

    return array


def connected(array, x, y):
    return find(array, x) == find(array, y)


def find(array, x):
    return array[x]


if __name__ == '__main__':
    n = 10
    # union = [(0, 1), (0, 2), (1, 3), (4, 8), (5, 6), (5, 7)]
    union = [(1, 2), (2, 5), (5, 6), (6, 7), (3, 8), (8, 9), (9, 4)]
    array = disjointSet(n, union)
    toCheck = [(1, 5), (5, 7), (4, 9)]
    for i, j in toCheck:
        print(connected(array, i, j))
    # checkConnectivity(disjointSet(n, union), [(0, 3), (1, 5), (7, 8)])

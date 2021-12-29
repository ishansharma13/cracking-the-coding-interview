"""
find the height of each node and then connect the values to the maximum node


(x1,y1) ==> find the rank/length of root of x1 and y1 each
if rank(rootX1)>rank(rootY1):
    then connect rootY1 to rootX1
else:
    connect rootX1 to rootY1
"""

class UnionRank:
    def __init__(self,size):
        self.array = list(range(size))
        self.rank = [1]*(size)


    def getRoot(self):
        return self.array

    def find(self,x):
        i = x
        while x!=self.array[x]:
            x = self.array[x]
        
        return x

    def connectivity(self,x,y):
        return self.find(x) == self.find(y)

    def union(self,x,y):
        rootX = self.find(x)
        rootY = self.find(y)

        if self.rank[rootX]> self.rank[rootY]:
            if self.array[rootY] == y:
                self.array[rootY] = rootX
        elif self.rank[rootY]> self.rank[rootX]:
            if self.array[rootX] == x:
                self.array[rootX] = rootY
        else:
            self.array[rootY] = rootX
            self.rank[rootX]+=1


if __name__ == '__main__':
    uf = UnionRank(5)
# 1-2-5-6-7 3-8-9 4
    # uf.union(1, 2)
    # uf.union(2, 5)
    # uf.union(5, 6)
    # uf.union(6, 7)
    # uf.union(3, 8)
    # uf.union(8, 9)
    uf.union(0,1)
    print(uf.getRoot())
    uf.union(0,2)
    print(uf.getRoot())
    uf.union(0,3)
    # print(uf.getRoot())
    # uf.union(2,3)
    # print(uf.getRoot())
    uf.union(1,4)
    print(uf.getRoot())
    # print(uf.connectivity(1, 5))  # true
    # print(uf.connectivity(5, 7))  # true
    # print(uf.connectivity(4, 9))  # false
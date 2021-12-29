class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        visited = []
        newVisited = []

        def dfs(node):
            visited.append(node)
            neighbors = set([x for x in node.neighbors])
            newNode = Node(node.val)
            newVisited.append(newNode)
            if neighbors.issubset(set(visited)) and node is None:
                return newNode
            else:
                for n in node.neighbors:
                    if n not in visited:
                        newNode.neighbors.append(dfs(n))
                    else:
                        for new in newVisited:
                            if n.val == new.val:
                                newNode.neighbors.append(new)
                        # visited.pop()
            return newNode

        x = dfs(node)
        print(visited)
        print(newVisited)
        return x


if __name__ == '__main__':
    adjList = [[2, 4], [1, 3], [2, 4], [1, 3]]

    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n1.neighbors = [n2, n4]
    n2.neighbors = [n1, n3]
    n3.neighbors = [n2, n4]
    n4.neighbors = [n1, n3]

    sol = Solution().cloneGraph(n1)
    print(sol.neighbors)

class UnionFind:
    def __init__(self, size):
        self.root = {i:i for i in range(size)}
        self.rank = [0] * size

    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])
            x = self.root[x]
        
        return x

    def union(self, x, y):
        rootx = self.find(x)
        rankx = self.rank[rootx]
        rooty = self.find(y)
        ranky = self.rank[rooty]

        if rootx != rooty:
            if rankx < ranky:
                self.root[rootx] = rooty
            elif ranky < rankx:
                self.root[rooty] = rootx
            else:
                self.root[rootx] = rooty
                self.rank[rootx] += 1


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        n = len(isConnected)
        dsu = UnionFind(n)

        components = n # the initial num of provinces 
        for citya in range(n):
            for cityb in range(citya + 1, n):
                if isConnected[citya][cityb] and dsu.find(citya) != dsu.find(cityb):
                    dsu.union(citya, cityb)
                    components -= 1
        
        return components 
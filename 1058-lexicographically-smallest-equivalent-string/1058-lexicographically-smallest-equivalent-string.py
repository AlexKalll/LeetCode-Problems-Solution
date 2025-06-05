class UnionFind: #
    def __init__(self, nodes):
        self.root = {node: node for node in nodes}

    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])  
        return self.root[x]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx == rooty:
            return
       
        if rootx < rooty:
            self.root[rooty] = rootx
        else:
            self.root[rootx] = rooty


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        all_chars = set(s1 + s2 + baseStr)
        dsu = UnionFind(all_chars)

        for c1, c2 in zip(s1, s2):
            dsu.union(c1, c2)

        return ''.join(dsu.find(c) for c in baseStr)

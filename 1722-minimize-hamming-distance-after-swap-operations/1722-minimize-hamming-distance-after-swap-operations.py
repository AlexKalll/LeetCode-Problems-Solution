class Solution:
    def minimumHammingDistance(self, s: List[int], t: List[int], sw: List[List[int]]) -> int:
        uf,zz = UnionFind(),defaultdict(Counter)
        for i,j in sw: uf.union(i,j)
        
        for i,v in enumerate(s): zz[uf.find(i)][v] += 1
        for i,v in enumerate(t): zz[p:=uf.find(i)][v] -= zz[p][v]>0
        
        return sum(z.total() for z in zz.values())

class UnionFind:
    def __init__(self):
        self.par = {}
    
    def union(self, el1, el2):
        self.par[self.find(el2)] = self.find(el1)

    def find(self, el):
        p = self.par.get(el, el)
        if p!=el: p = self.par[el] = self.find(p)
        return p
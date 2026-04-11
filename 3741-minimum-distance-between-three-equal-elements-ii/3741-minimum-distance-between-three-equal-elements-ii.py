class Solution:
    def minimumDistance(self, a: List[int]) -> int:
        d = defaultdict(list)
        for i,v in enumerate(a): d[v].append(i)
        return min(((k-i)*2 for l in d.values() for i,k in zip(l,l[2:])),default=-1)
class Solution:
    def reverseSubmatrix(self, g: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        for r1,r2 in zip(g[x:x+k//2],g[x+k-1:x+k//2-1:-1]):
            r1[y:y+k],r2[y:y+k] = r2[y:y+k],r1[y:y+k]
        return g
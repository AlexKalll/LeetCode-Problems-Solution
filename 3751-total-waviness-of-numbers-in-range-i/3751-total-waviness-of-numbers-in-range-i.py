class Solution:
    def totalWaviness(self, l: int, r: int) -> int:
        return sum(p*q<0 for v in range(l,r+1) 
            for p,q in pairwise(starmap(sub,pairwise(map(int,str(v))))))
"""
class Solution:
    def coloredCells(self, n: int) -> int:
        ans  = 1
        i = 0
        
        while i < n:
            ans += (i * 4)
            i += 1
        
        return ans
"""
class Solution:
    def coloredCells(self, n: int) -> int:
        return 2*n*(n-1)+1


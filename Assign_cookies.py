#https://leetcode.com/problems/assign-cookies/
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        count = 0
        i, j =  0, 0
        while j < len(s) and i < len(g):
            if s[j] >= g[i]:
               count += 1
               i += 1
            j += 1
        return count

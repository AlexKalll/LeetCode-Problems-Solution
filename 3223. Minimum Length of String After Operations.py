# https://leetcode.com/problems/minimum-length-of-string-after-operations/

class Solution:
    def minimumLength(self, s: str) -> int:
        cnt = Counter(s)
        n = len(s)
        for c in cnt:
            if cnt[c] % 2 == 0:
                n -= (cnt[c] -2) 
            else:
                n -= (cnt[c] - 1)
        
        return n

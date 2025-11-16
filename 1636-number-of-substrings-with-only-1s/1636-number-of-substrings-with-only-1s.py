class Solution:
    def numSub(self, s: str) -> int:
        M = 1_000_000_007
        ans = 0
        count1 = 0

        for ch in s:
            if ch == '1':
                count1 += 1
                ans = (ans + count1) % M
            else:
                count1 = 0
        
        return ans
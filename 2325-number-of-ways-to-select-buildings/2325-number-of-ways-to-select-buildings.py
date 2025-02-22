class Solution:
    def numberOfWays(self, s: str) -> int:
        ones = s.count('1')
        zeros = len(s) - ones
        
        zero_prefix = one_prefix = 0
        ans = 0

        for bit in s:
            if bit == '1':
                ans += zero_prefix * (zeros - zero_prefix)
                one_prefix += 1
            else:
                ans += one_prefix * (ones - one_prefix)
                zero_prefix += 1

        return ans
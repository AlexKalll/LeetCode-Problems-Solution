class Solution:
    def minimumSteps(self, s: str) -> int:

        num_ones = 0 # to count the # of ones before the current zero
        ans = 0

        for binary in s:
            if binary == "1": 
                num_ones += 1
            else:
                ans += num_ones # No- of flips required to take the currnet zero to a position before all ones
        
        return ans 
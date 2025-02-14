class Solution:
    def minimumSteps(self, s: str) -> int:
        num_ones = 0
        ans = 0

        for binary in s:
            if binary == "1":
                num_ones += 1
            else:
                ans += num_ones
        
        return ans 
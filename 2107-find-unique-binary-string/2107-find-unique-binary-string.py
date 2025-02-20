class Solution:
    def findDifferentBinaryString(self, nums):
        n = len(nums)
        ans = "0" * n  # Start with "000...0"
        
        if ans not in nums:
            return ans
        
        ans = list(ans)
        for i in range(n):
            ans[i] = '1'  # Try flipping one bit at a time
            if "".join(ans) not in nums:
                return "".join(ans)
            ans[i] = '0'  # Revert back if needed
        
        return "".join(ans)  # Fallback case
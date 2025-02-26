class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        curr = 0
        ht = {0: -1}
        ans = 0

        for i, num in enumerate(nums):
            curr += 1 if num == 1 else -1
            if curr in ht:
                ans = max(ans, i - ht[curr])
            else:
                ht[curr] = i
        
        return ans 
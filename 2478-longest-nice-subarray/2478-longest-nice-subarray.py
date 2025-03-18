class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        max_len = 1 
        nice = set()

        for r in range(n):
            while any((nums[r] & num) != 0 for num in nice):
                nice.remove(nums[left])
                left += 1
            
            nice.add(nums[r])
            max_len = max(max_len, r - left + 1)
        
        return max_len
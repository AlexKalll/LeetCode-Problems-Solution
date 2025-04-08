class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        count = 0
        while l < n and len(set(nums[l:n])) < n - l:
            l += 3
            count += 1
        return count
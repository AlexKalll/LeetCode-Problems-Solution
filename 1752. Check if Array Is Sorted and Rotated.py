# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/

class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        
        x = nums.index(min(nums))
        if x == 0:
            j = n-1
            while j >= 0 and nums[j] == nums[0]:
                x = j
                j -= 1

        return nums[x:n] + nums[0:x] == sorted(nums)

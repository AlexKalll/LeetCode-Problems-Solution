class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        left_sum, right_sum = 0, sum(nums)

        for i, num in enumerate(nums):
            if left_sum == right_sum - left_sum - num:
                return i
            left_sum += num
            
        return -1
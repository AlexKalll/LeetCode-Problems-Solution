class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left = 0
        res = 0
        current_set = set()
        current_sum = 0
        for i, num in enumerate(nums):
            while num in current_set:
                current_set.remove(nums[left])
                current_sum -= nums[left]
                left += 1

            current_set.add(num)
            current_sum += num
            res = max(res, current_sum)

        return res

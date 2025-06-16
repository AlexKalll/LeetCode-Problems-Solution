class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max_diff = -1
        min_value = nums[0]

        for j in range(1, len(nums)):
            # Update min_value
            min_value = min(min_value, nums[j - 1])
            
            # Calculate the difference
            if nums[j] > min_value:
                max_diff = max(max_diff, nums[j] - min_value)

        return max_diff
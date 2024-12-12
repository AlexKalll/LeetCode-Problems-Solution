class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()  # Sort the array
        left = 0  # Initialize the left pointer
        
        for right in range(len(nums)):
            # Check if the current window can be adjusted to be equal
            if nums[right] - nums[left] > 2 * k:
                left += 1  # Move the left pointer to shrink the window
        
        # The maximum beauty is the size of the valid window
        return len(nums) - left

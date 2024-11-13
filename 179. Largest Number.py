class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n = len(nums)

        # Convert integers to strings for comparison
        for i in range(n):
            nums[i] = str(nums[i])
        
        # Sort based on concatenated string comparison
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[j] + nums[i] > nums[i] + nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]  # Swap if in wrong order
        
        # Join and convert to int to remove leading zeros, then back to string
        return str(int(''.join(nums)))

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        
        # Calculate prefix sums
        for index in range(n):
            prefix_sum[index + 1] = prefix_sum[index] + nums[index]
        
        count = 0
        left = 0
        
        # Use sliding window to count valid subarrays
        for right in range(n):
            while left < n and (prefix_sum[left + 1] - prefix_sum[right]) * (left - right + 1) < k:
                left += 1
            count += left - right
        
        return count

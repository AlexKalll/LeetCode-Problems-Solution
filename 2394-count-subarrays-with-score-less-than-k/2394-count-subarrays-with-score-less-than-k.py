class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        
        # Calculate prefix sums
        for index in range(n):
            prefix_sum[index + 1] = prefix_sum[index] + nums[index]
        
        count = 0
        right = 0  # Renamed from j to right
        
        # Use sliding window to count valid subarrays
        for left in range(n): 
            while right < n and (prefix_sum[right + 1] - prefix_sum[left]) * (right - left + 1) < k:
                right += 1
            count += right - left
        
        return count
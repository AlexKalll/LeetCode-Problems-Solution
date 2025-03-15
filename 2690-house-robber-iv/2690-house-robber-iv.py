class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def canRobWithCapability(capability: int) -> bool:
            count = 0
            i = 0
            
            while i < len(nums):
                if nums[i] <= capability:
                    count += 1
                    i += 1  # Skip the next house
                i += 1  # Move to the next house
            
            return count >= k
        
        left, right = min(nums), max(nums)
        result = right
        
        while left <= right:
            mid = (left + right) // 2
            
            if canRobWithCapability(mid):
                result = mid  # Update result to the current mid
                right = mid - 1  # Try for a smaller capability
            else:
                left = mid + 1  # Increase capability
        
        return result

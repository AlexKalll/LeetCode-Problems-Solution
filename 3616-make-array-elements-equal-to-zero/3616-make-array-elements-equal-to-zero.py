class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n = len(nums)
        valid_count = 0
        
        for curr in range(n):
            if nums[curr] == 0:
                # Try moving left
                if self.canZeroAll(nums[:], curr, -1):  # Copy the list to avoid modifying the original
                    valid_count += 1
                # Try moving right
                if self.canZeroAll(nums[:], curr, 1):  
                    valid_count += 1
        
        return valid_count
    
    def canZeroAll(self, nums: List[int], curr: int, direction: int) -> bool:
        n = len(nums)
        
        while 0 <= curr < n:
            if nums[curr] == 0:
                curr += direction  # Move in the current direction
            else:
                nums[curr] -= 1  # Decrement the value
                direction *= -1  # Reverse the direction
                curr += direction  # Move in the new direction
        
        return all(num == 0 for num in nums)
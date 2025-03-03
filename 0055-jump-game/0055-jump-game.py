class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        max_idx = 0
        for i in range(len(nums)):
            if max_idx < i:
                return False

            max_idx = max(max_idx, i + nums[i])
            
        return max_idx >= len(nums)-1
        
        
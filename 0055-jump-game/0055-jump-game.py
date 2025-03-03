class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        # max_idx = 0
        # for i in range(len(nums)):
        #     if max_idx < i:
        #         return False

        #     max_idx = max(max_idx, i + nums[i])
            
        # return max_idx >= len(nums)-1

        n = len(nums)
        max_idx  = 0 

        for i in range(n):
            if max_idx < i:
                return False
            
            curr = i + nums[i]
            max_idx = max(max_idx, curr)
        
        return True
        
        
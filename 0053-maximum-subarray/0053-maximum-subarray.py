class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        curr_max = nums[0]

        # applying kadane's algorithm
        for i in range(1, len(nums)):
            
            curr_max = max(curr_max + nums[i], nums[i])
            ans = max(ans, curr_max)
        
        return ans
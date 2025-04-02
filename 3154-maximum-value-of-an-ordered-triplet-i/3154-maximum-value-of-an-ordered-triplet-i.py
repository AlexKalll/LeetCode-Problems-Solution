class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_value = float('-inf')  
        
        n = len(nums)
        
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    value = (nums[i] - nums[j]) * nums[k]
                    max_value = max(max_value, value)
        
        return max(max_value, 0)
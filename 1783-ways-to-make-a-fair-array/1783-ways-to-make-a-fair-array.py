class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        even_sum = sum(nums[i] for i in range(0, len(nums), 2))
        odd_sum = sum(nums[i] for i in range(1, len(nums), 2))
        
        count = 0
        curr_even = 0
        curr_odd = 0
        
        for i in range(len(nums)):
            if i % 2 == 0: 
                even_sum -= nums[i]
            else:  
                odd_sum -= nums[i]
            
            if curr_even + odd_sum == curr_odd + even_sum:
                count += 1
            
            if i % 2 == 0:
                curr_even += nums[i]
            else:
                curr_odd += nums[i]
        
        return count
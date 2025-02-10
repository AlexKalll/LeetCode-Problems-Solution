class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n = len(nums)
        for i in range(n):
            nums[i] = str(nums[i])
        
        for i in range(n-1):
            for j in range(i + 1, n):
                if nums[j] + nums[i] > nums[i] + nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]  # swap them 
                
                # else: do nothing 
        return str(int(''.join(nums)))
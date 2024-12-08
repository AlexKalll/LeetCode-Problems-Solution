class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        result = []
        n = len(nums)
        for i in range(n):
            if nums[i] > 0:
                landing = (i + nums[i]) % n
                result.append(nums[landing])
            elif nums[i] < 0:
                landing = (i + nums[i]) % n
                result.append(nums[landing])      
            else: 
                result.append(nums[i])
            
        return result©leetcode

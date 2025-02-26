class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        prefix = [nums[0]]

        for i in range(1, len(nums)):
            prefix.append(prefix[i-1] + nums[i])
        
        max_p = max(prefix )
        min_p = min(prefix)

        # print(prefix)
        # print(max_p) 
        # print(min_p)

        ans = max_p - min_p 
        
        if abs(min_p) > ans:
            return abs(min_p)

        if abs(max_p) > ans:
            return abs(max_p)

        return ans
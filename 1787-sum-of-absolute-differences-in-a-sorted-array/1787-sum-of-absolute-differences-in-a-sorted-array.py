class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pf = [nums[0]]

        for i in range(1, n):
            pf.append(pf[i-1] + nums[i])

        for i in range(n):
            left_sum = abs(pf[i] - (nums[i] * (i + 1)))
            right_sum = abs(pf[-1] - pf[i] - (nums[i] * (n - i -1) ))
            nums[i] =  left_sum + right_sum 
        
        return nums
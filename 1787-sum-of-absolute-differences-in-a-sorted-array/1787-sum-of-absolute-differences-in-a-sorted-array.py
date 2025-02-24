class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        l, n = 0, len(nums)
        ans = []
        prefix_sum = [0] * n
        prefix_sum[0] = nums[0]
        
        for i in range(1, n):
            prefix_sum[i] = nums[i] + prefix_sum[i-1]

        for i in range(n):
            left_sum = (nums[i] * (i+1) - prefix_sum[i])
            right_sum = prefix_sum[-1]  - prefix_sum[i] - (nums[i] *(n-i-1))

            ans.append(right_sum + left_sum)

        return ans 
            
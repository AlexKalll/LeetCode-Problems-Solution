class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        pref_sum = [0] * (n + 1)

        # making exclusive prefix sum 
        for i in range(1, len(pref_sum)):
            pref_sum[i] += (pref_sum[i-1] + nums[i-1])

        for i in range(1, len(pref_sum)):
            if pref_sum[i-1] == (pref_sum[-1] - pref_sum[i]):
                return i - 1
        
        return -1
class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        bits = [-1]*32
        res = []
        n = len(nums)
        for i in range(n-1,-1,-1):
            for j in range(32):
                if nums[i] & (1<<j) != 0:
                    bits[j] = i
            val = max(bits)+1-i
            res.insert(0,max(val,1))
        return res
        
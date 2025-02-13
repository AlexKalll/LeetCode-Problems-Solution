class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans = sum(nums[:k])
        curr = ans 

        for r in range(k, len(nums)):
            curr -= nums[r-k]
            curr += nums[r]
            ans = max(ans, curr)

        return ans/k

        
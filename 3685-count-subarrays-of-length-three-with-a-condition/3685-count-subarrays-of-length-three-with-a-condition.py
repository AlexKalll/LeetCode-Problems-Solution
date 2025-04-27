class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        print(-7//2)
        for i in range(2, n):
            if nums[i-2] + nums[i] == nums[i-1]//2 and nums[i-1] % 2 == 0:
                count += 1

        return count
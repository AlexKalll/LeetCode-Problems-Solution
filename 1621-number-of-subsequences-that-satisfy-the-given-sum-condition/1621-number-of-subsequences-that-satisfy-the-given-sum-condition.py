class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        mod = 10**9 + 7
        left, right = 0, len(nums) - 1
        result = 0
        
        power = [1] * (len(nums) + 1)
        
        for i in range(1, len(nums) + 1):
            power[i] = (power[i - 1] * 2) % mod
        
        while left <= right:
            if nums[left] + nums[right] <= target:
                result = (result + power[right - left]) % mod
                left += 1
            else:
                right -= 1
        
        return result

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        largest = max(nums)
        left = 0
        ans = 0
        count = 0

        for right in range(len(nums)):
            count += 1 if nums[right] == largest else 0
            while count == k:
                ans += (len(nums) - right)
                if nums[left] == largest:
                    count -= 1
                left += 1

        return ans
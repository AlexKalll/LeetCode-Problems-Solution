class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        """maxbitwise = max(nums)
        ans = 1 # since there is the max num at minimum

        for i in range(len(nums)):
            count = 0
            if nums[i] == maxbitwise:
                while i < len(nums) and nums[i] == maxbitwise:
                    count += 1
                    i += 1
                ans = max(ans, count)
            # print(i)
        return ans """

        # using two pointer technique 
        ans = 1 # since we already have atleast one ans that is the max value from the list 
        maxbitwise = max(nums)

        left = 0

        for right in range(len(nums)):
            if nums[right] == maxbitwise:
                ans = max(ans, right - left + 1)
            else:
                left = right + 1
        return ans 

# in both cases the time and space complexities are O(n) and O(1) respectively.

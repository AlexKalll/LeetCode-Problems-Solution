class Solution(object):
    def splitArray(self, nums, k):

        def validator(target):
            count = 1
            prefix = 0
            for i in range(len(nums)):
                prefix += nums[i]
                if prefix > target:
                    prefix = nums[i]
                    count += 1
            return count <= k

        low,high = max(nums),sum(nums)
        while low <= high:
            mid = (low+high)//2
            if validator(mid):
                high = mid-1
            else:
                low = mid+1
        return low
        

        
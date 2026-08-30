class Solution(object):

    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        min_idx = 0
        max_idx = 0

        for i in range(1, n):
            if nums[min_idx] > nums[i]:
                min_idx = i

            if nums[max_idx] < nums[i]:
                max_idx = i

        right = max(min_idx, max_idx)
        left = min(min_idx, max_idx)

        res = right + 1
        res = min(res, n - left)
        res = min(res, (left + 1) + (n - right))

        return res
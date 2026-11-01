class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minNum = float('inf')

        for n in nums:
            minNum = min(minNum, n)

        count = 0

        for n in nums:
            count += n - minNum

        return count
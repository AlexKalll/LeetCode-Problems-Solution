class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0

        for i in range(n - 2):
            if nums[i] == 0:
                for j in range(i, i+3):
                    nums[j] = 1 if nums[j] == 0 else 0
                count += 1

        if len(set(nums)) == 1:
            return count 
        else:
            return -1

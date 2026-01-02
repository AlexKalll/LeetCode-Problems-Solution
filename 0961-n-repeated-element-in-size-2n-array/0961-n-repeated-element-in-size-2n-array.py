class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        
        return next(num for num, count in Counter(nums).items() if count >1)
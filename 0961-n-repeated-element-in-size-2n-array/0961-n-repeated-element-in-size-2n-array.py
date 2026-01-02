class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        ht = Counter(nums)
        for num in ht:
            if ht[num] > 1:
                return num 
                
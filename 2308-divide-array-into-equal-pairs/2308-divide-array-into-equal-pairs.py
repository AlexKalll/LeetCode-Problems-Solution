class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        ht = Counter(nums)
        for num in ht:
            if ht[num] % 2 != 0:
                return False
        
        return True
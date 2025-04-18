class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ht = Counter(nums)
        missed = duplicated = -1

        for num in range(1, n+1):
            if num not in ht:
                missed = num
            if ht[num] == 2:
                duplicated = num
        
        return [duplicated, missed]

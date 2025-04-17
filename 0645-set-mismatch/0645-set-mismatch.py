class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        num_count = {}
        duplicate = missing = -1

        for num in nums:
            if num in num_count:
                num_count[num] += 1
            else:
                num_count[num] = 1
    
        for i in range(1, len(nums) + 1):
            if i in num_count:
                if num_count[i] == 2:
                    duplicate = i
            else:
                missing = i
        
        return [duplicate, missing]
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        res = nums[0]
        count = 0

        for num in nums:
            if num == res:
                count += 1
            else:
                count -= 1
                if count <= 0:
                    res = num
                    count = 1

        return res
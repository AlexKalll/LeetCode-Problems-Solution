from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        total_xor_sum = 0

        def backtrack(curr, start):
            nonlocal total_xor_sum
            if start == n:
                xor_value = 0
                for num in curr:
                    xor_value ^= num
                total_xor_sum += xor_value
                return 

            backtrack(curr + [nums[start]], start + 1)
            
            backtrack(curr, start + 1)

        backtrack([], 0)
        return total_xor_sum

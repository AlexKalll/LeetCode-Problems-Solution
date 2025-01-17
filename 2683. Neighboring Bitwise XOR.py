# https://leetcode.com/problems/neighboring-bitwise-xor/description

class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        n = len(derived)
        
        # Assume original[0] = x
        # We will compute the rest of the original array based on this assumption
        original = [0] * n
        original[0] = 0  # Starting with x = 0
        
        # Calculate the rest of the original array
        for i in range(1, n):
            original[i] = original[i - 1] ^ derived[i - 1]
        
        # Check the last condition
        last_condition = original[n - 1] ^ original[0]
        
        return last_condition == derived[n - 1]

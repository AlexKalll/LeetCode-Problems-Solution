class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        values_per_modulo = [0] * value
        for n in nums:
            values_per_modulo[n % value] += 1
        
        min_value = min(values_per_modulo)
        min_index = values_per_modulo.index(min_value)

        return value * min_value + min_index
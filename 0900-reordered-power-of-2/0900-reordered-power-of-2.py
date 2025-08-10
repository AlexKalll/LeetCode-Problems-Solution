from collections import Counter

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        digit_count = Counter(str(n))

        for i in range(31):
            power_of_2 = 2 ** i
            if Counter(str(power_of_2)) == digit_count:
                return True
        
        return False
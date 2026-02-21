class Solution:
    def countPrimeSetBits(self, l: int, r: int) -> int:
        return sum(v.bit_count() in (2,3,5,7,11,13,17,19) for v in range(l,r+1))
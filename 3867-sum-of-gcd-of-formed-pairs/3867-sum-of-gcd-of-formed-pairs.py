class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        pgcd = sorted(map(gcd, nums, accumulate(nums, max)))  # prefixGcd calculation
        return sum(map(gcd, islice(pgcd, len(nums) // 2), reversed(pgcd)))  # pairs match + sum of gcd
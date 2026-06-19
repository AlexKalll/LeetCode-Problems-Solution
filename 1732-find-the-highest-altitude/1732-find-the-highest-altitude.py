class Solution:
    def largestAltitude(self, a: List[int]) -> int:
        return max(accumulate([0]+a))
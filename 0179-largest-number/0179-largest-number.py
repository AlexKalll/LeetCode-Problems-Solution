class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        return str(int("".join(map(str, sorted(nums, key=lambda num: str(num) * 10, reverse=True)))))
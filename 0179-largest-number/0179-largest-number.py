class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums.sort(key=lambda num: str(num) * 10, reverse=True)
        return str(int("".join(map(str, nums))))
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums.sort(key=lambda num: str(num) * 10, reverse=True)
        answer = "".join(map(str, nums))
        return answer[:-1].lstrip("0") + answer[-1]
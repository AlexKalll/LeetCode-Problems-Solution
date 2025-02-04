class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        rem = num % 3
        mid = num // 3
        if rem == 0:
            return [mid-1, mid, mid+1]
        else:
            return []
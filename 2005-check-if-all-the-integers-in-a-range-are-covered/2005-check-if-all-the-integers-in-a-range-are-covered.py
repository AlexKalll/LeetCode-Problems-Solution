class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
       
        for i in range(left, right + 1):
            for a, b in ranges:
                if a <= i <= b:
                    break
            else:
                return False
        return True

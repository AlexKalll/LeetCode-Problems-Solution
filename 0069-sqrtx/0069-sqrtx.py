class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x//2 if x >= 4 else x
        
        while left <= right:
            mid = (left + right) // 2
            curr = mid*mid

            if curr <= x:
                left = mid + 1
            elif curr > x:
                right = mid - 1
            
        return right
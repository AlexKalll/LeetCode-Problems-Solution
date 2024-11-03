class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 10:
            l, r = 1, x
        else:
            l, r = 1, x // 2
        
        while l < r:
            mid = (l + r) // 2
            mid_squared = mid * mid
            
            if mid_squared < x:  # Mid is too small
                l = mid + 1  # Move to the right
            else:  # Mid is too large or equal
                r = mid  

        return l - 1 if l * l > x else l

"""
# just using simple binary search 
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 10:
            l, r = 1, x
        else:
            l, r = 1, x // 2
        
        while l <= r:
            mid = (l + r) // 2
            mid_squared = mid * mid
            
            if mid_squared == x:  # Perfect square
                return mid
            elif mid_squared < x:  # Mid is too small
                l = mid + 1
            else:  # Mid is too large
                r = mid - 1
        
        return r  # r is the largest integer whose square is <= x
"""

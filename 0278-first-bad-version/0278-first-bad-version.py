# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        left =  1
        right = n
        while left <= right:
            mid = (left + right) //  2
            
            if isBadVersion(mid):
                right = mid -1
            else:
                left = mid + 1
            
        return left
        
"""
        left =  1
        right = n

        while left <= right:
            mid = (left + right) //  2
            
            if isBadVersion(mid):
                first_bad = mid
                right = mid -1
            else:
                left = mid + 1
            
        return first_bad
"""
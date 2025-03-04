class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        lcnt = 0
        rcnt = 0

        for char in s:
            if char == 'L':
                lcnt += 1
            else:
                rcnt += 1
            
            if lcnt == rcnt:
                count += 1
        
        return count
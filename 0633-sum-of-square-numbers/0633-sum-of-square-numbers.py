class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l = 0
        r = int(math.sqrt(c))

        while l <= r:
            curr = r**2 + l**2
            print(curr)
            if curr == c:
                return True
            elif curr < c:
                l += 1
            else:
                r -= 1
        
        return False
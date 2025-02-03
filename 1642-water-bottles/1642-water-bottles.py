class Solution:
    def numWaterBottles(self, n: int, m: int) -> int:
        # n = numBottles   and   m = numExchange
        ans = n
        
        while n // m > 0:
            ans += (n//m)
            n = (n//m) + (n%m)

        return ans 
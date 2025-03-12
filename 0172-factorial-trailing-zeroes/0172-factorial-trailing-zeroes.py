"""class Solution:
    def trailingZeroes(self, n: int) -> int:
        
        fact = factorial(n)

        ans = 0
        while fact % 10 == 0:
            fact //= 10
            ans += 1
        
        return ans 
    """

class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n >= 5:
            n //= 5
            count += n
        return count


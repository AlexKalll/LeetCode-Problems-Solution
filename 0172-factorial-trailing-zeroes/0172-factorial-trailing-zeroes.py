class Solution:
    def trailingZeroes(self, n: int) -> int:
        
        def factorial(n):
            if n <= 1:
                return 1
            
            return n * factorial(n-1)

        fact = factorial(n)

        ans = 0
        while fact % 10 == 0:
            fact //= 10
            ans += 1
        
        return ans 
        
        
        
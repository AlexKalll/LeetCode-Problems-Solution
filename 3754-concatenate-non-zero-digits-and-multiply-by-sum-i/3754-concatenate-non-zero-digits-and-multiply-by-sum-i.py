class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x,s,c = 0,0,0
        while n:
            s += (d:= n%10)
            x += d * 10**c
            c += (d != 0)
            n //=10
        return x*s
        
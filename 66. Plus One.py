# https://leetcode.com/problems/plus-one/description/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # First let's change the digits to larger integer
        num = 0
        for digit in digits:
            num = num * 10 + digit
        num += 1
        # Secondly, change the integer into digits array and return it
        digits.clear()
        while num > 0:
            digit = num % 10
            digits.insert(0, digit)
            num //= 10
        return digits
       

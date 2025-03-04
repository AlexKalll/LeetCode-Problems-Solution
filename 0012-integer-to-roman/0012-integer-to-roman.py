class Solution:
    def intToRoman(self, num: int) -> str:
        value_symbols = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'),
            (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        
        ans = []
        for val, symbol in value_symbols:
            if num == 0:
                break
            cnt = num // val
            ans.append(symbol * cnt)
            num -= val*cnt
        
        return ''.join(ans)
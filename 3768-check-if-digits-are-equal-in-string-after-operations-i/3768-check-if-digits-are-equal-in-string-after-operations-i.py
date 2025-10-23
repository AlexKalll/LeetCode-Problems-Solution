class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) > 2:
            new_s = ""
            for i in range(len(s) - 1):
                sum = (int(s[i]) + int(s[i+1])) % 10
                new_s += str(sum)
            s = new_s
        return s[0] == s[1]

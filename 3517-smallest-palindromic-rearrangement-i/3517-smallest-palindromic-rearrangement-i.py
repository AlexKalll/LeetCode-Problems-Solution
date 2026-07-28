class Solution:
    def smallestPalindrome(self, s: str) -> str:
        c: List[int] = [0] * 26
        for x in s:
            c[ord(x) - ord('a')] += 1

        l = ""
        m = ""
        for i in range(26):
            l += chr(ord('a') + i) * (c[i] // 2)
            if c[i] % 2 == 1:
                m = chr(ord('a') + i)

        r = l[::-1]
        return l + (m if m else "") + r

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        freq = [0] * 26
        for c in s:
            freq[ord(c) - ord('a')] += 1
        
        mid = ''
        half = [0] * 26
        total = 0
        for i in range(26):
            half[i] = freq[i] // 2
            total += half[i]
            if freq[i] % 2 == 1:
                mid = chr(i + ord('a'))
        
        h = half[:]
        total_perms = self.calculate_perms(h, total)
        if k > total_perms:
            return ""
        
        left = ""
        while total:
            for i in range(26):
                if h[i]:
                    h[i] -= 1
                    w = self.calculate_perms(h, total - 1)
                    if w >= k:
                        left += chr(i + ord('a'))
                        total -= 1
                        break
                    else:
                        k -= w
                        h[i] += 1
        
        right = left[::-1]
        return left + (mid if mid else "") + right

    def calculate_perms(self, h: List[int], total: int) -> int:
        res = 1
        for count in h:
            if count:
                res *= self.combine(total, count)
                if res > 1000001:
                    res = 1000001
                total -= count
        return res

    def combine(self, n: int, r: int) -> int:
        if r > n:
            return 0
        res = 1
        for i in range(1, r + 1):
            res = res * (n - r + i) // i
            if res > 1000001:
                return 1000001
        return res

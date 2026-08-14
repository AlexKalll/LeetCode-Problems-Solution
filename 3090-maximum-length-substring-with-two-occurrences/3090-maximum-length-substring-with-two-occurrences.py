class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        l = 0
        ans = 0
        freq = {}

        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1

            while freq[s[r]] > 2:
                freq[s[l]] -= 1
                l += 1

            ans = max(ans, r - l + 1)

        return ans
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        ans = 0
        char_count = set()

        for right, char in enumerate(s):
            if char not in char_count:
                char_count.add(char)
            else:
                while char in char_count:
                    char_count.remove(s[left])
                    left += 1
                char_count.add(char)
            ans = max(ans, right - left + 1)

        return ans

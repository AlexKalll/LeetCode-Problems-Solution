class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        ans = 0
        char_set = set()

        for right, char in enumerate(s):
            while char in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(char)
            ans = max(ans, right - left + 1)

        return ans

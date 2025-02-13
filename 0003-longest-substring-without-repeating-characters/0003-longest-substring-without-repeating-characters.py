class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        ans = 0
        char_count = defaultdict(int)

        for right, char in enumerate(s):
            char_count[char] += 1

            while char_count[char] > 1:
                char_count[s[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans




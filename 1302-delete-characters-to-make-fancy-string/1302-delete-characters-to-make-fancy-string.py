class Solution:
    def makeFancyString(self, s: str) -> str:
        result = []
        for i in range(len(s)):
            # Only add character if the last two characters are not same as current
            if len(result) >= 2 and result[-1] == s[i] and result[-2] == s[i]:
                continue
            result.append(s[i])
        return ''.join(result)

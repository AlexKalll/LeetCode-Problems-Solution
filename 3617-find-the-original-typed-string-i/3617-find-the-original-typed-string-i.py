class Solution:
    def possibleStringCount(self, word: str) -> int:
        res = 1
        i = 0
        l = len(word)
        while i < l:
            val = 1
            cur = word[i]
            while i < l - 1 and cur == word[i + 1]:
                val += 1
                i += 1
            i += 1
            res += val - 1
        return res
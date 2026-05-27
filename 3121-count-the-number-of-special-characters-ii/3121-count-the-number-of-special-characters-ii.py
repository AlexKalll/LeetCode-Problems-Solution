class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        n = len(word)
        last, first = {}, {}
        for i in range(n):
            if word[i].isupper() and word[i] not in first:
                first[word[i]] = i
            last[word[i]] = i
            
        return sum(first.get(u, -1) > last.get(l, n) for u, l in zip(ascii_uppercase, ascii_lowercase))
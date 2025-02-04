class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        cnt = Counter(s)
        curr = cnt[s[0]]
        for c in cnt:
            if cnt[c] != curr:
                return False
        
        return True
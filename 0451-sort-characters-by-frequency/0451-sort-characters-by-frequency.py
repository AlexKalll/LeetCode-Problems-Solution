class Solution:
    def frequencySort(self, s: str) -> str:
        ht = Counter(s)
        mp = dict(sorted(ht.items(), key = lambda x: (x[1]), reverse = True))
        
        ans = ''
        for c in mp:
            ans += c * mp[c]

        return ans 
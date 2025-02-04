class Solution:
    def firstUniqChar(self, s: str) -> int:

        hT = defaultdict(list)
        for i in range(len(s)):
            hT[s[i]].append(i)
        
        for c in hT:
            if len(hT[c]) == 1:
                return hT[c][0]
        
        return -1
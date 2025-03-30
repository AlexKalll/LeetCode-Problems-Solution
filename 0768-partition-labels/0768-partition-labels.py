class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # hash table
        n = len(s)
        ht = Counter(s)
        mp = Counter(s)

        l  = 0
        count = 0
        ans = []

        for r, c in enumerate(s):
            print(ht[c], mp[c])
            if ht[c] == mp[c]:
                count += 1

            ht[c] -= 1
            if ht[c] == 0:
                del ht[c]
                count -= 1
            
            if count == 0:
                ans.append(r-l+1)
                l = r + 1

        return ans 
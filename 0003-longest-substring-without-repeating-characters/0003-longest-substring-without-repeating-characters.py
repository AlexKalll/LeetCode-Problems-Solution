class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        ht = defaultdict(int)
        ans = 0

        for r in range(len(s)):
            ht[s[r]] += 1
            if ht[s[r]] == 1:
                ans = max(ans, r - l + 1)
           
            else:
                while ht[s[r]] > 1:      
                    ht[s[l]] -= 1
                    if ht[s[l]] == 0:
                        del ht[s[l]]
                    l += 1
                         
        
        return ans

    
        

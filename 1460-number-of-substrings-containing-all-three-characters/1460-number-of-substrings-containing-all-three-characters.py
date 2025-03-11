class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left = 0
        count = {}
        total_substrings = 0
        
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            
            while len(count) == 3:  
                total_substrings += len(s) - right 
                
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    del count[s[left]]
                left += 1
        
        return total_substrings

# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'
        ans = 0
        count = 0
        for i in range(k):
            if s[i] in vowels:
                count += 1
        ans = count  
        
        for i in range(1, len(s) - k + 1): 
            if s[i-1] in vowels:
                count -= 1
            if s[i+k - 1] in vowels:
                count += 1
                
            ans = max(ans, count)
            
        return ans


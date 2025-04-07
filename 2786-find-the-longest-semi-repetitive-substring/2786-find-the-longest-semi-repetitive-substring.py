class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        max_length = 0
        n = len(s)

        for i in range(n):
            count = 0
            current_length = 1
            
            for j in range(i + 1, n):
                if s[j] == s[j - 1]:
                    count += 1
                if count > 1:
                    break
                current_length += 1
            
            max_length = max(max_length, current_length)
        
        return max_length

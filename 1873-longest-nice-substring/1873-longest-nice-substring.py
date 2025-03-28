class Solution:
    def longestNiceSubstring(self, s: str) -> str:

        def dvqr(s):
            sets = set(s)
            if len(s) <= 1:
                return ''
            
            for i in range(len(s)):
                curr = s[i]
     
                if curr.swapcase() not in sets:
                    left = dvqr(s[:i])
                    right = dvqr(s[i + 1:])

                    if len(left) >= len(right):
                        return left
                    return right 
                
            return s  

        return dvqr(s)

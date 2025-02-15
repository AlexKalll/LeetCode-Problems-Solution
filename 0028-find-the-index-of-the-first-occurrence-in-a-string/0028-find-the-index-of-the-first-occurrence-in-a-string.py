class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if needle not in haystack:
            return -1 
        
        n = len(needle)
        for i in range(len(haystack)):
            if needle == haystack[i:i+n]:
                return i
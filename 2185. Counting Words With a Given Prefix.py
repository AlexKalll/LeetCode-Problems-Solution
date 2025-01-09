# https://leetcode.com/problems/counting-words-with-a-given-prefix

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        ans = 0
        for word in words:
            if word.startswith(pref):
                ans += 1
        
        return ans 

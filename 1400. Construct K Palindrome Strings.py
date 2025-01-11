# https://leetcode.com/problems/construct-k-palindrome-strings

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        # Count the frequency of each character
        char_count = Counter(s)
        
        # Count how many characters have an odd frequency
        odd_count = sum(1 for count in char_count.values() if count % 2 != 0)
        
        # We can form k palindromes if we have at most k odd counts having at least k characters in the given string s
        return odd_count <= k and k <= len(s)

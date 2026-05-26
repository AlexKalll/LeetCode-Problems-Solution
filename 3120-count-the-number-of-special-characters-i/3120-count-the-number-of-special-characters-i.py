class Solution:
    def numberOfSpecialChars(self, w: str) -> int:
        return (s:={*w}) and sum(c.upper() in s for c in s if c.islower())
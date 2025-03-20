class Solution:
    def splitString(self, s: str) -> bool:
        def backtrack(start, curr):
            if start >= len(s):
                for i in range(1, len(curr)):
                    if curr[i-1] - curr[i] != 1:
                        return False

                return len(curr) >= 2
        
            for i in range(start, len(s)):
                x = int(s[start: i + 1])
                if curr and curr[-1] - x != 1:
                    continue
                curr.append(x)
                if backtrack(i + 1, curr):
                    return True
                curr.pop()
            
            return False
        
        return backtrack(0, [])

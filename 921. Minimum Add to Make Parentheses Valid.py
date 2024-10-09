class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for c in s:
            if not stack or c =='(':
                stack.append(c)
            else:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(c)
                    
        return len(stack)

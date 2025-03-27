"""class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(curr, open_count, close_count):
            if len(curr) == 2*n:
                ans.append(''.join(curr))
                return 
            
            if open_count < n:
                curr.append('(')
                backtrack(curr, open_count + 1, close_count)
                curr.pop()

            if close_count < open_count:
                curr.append(')')
                backtrack(curr, open_count , close_count+ 1)
                curr.pop() 
        
        backtrack([], 0, 0)
        return ans 
    """
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(curr, open_count, close_count):
            if len(curr) == 2*n:
                ans.append(''.join(curr))
                return 
        
            for par in '()':
                if par == '(' and open_count >= n:
                    continue
                if par == ')' and close_count >= open_count:
                    continue
                
                curr.append(par)
                if par == '(':
                    backtrack(curr, open_count + 1, close_count)
                if par == ')':
                    backtrack(curr, open_count , close_count+ 1)
            
                curr.pop()

        backtrack([], 0, 0)
        return ans

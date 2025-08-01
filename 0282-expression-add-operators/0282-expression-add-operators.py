class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        ops = ["*", "+", "-"]
        
        def fn(i): 
            """Populate ans with a stack via backtracking."""
            stack.append(num[i]) 
            if i == len(num)-1: 
                expr = "".join(stack)
                if eval(expr) == target: ans.append(expr)
            else: 
                for op in ops + [""]:
                    if stack[-1] == "0" and op == "" and (len(stack) == 1 or stack[-2] in ops): continue 
                    stack.append(op) 
                    fn(i+1)
                    stack.pop() 
            stack.pop() 
        
        ans, stack = [], []
        fn(0)
        return ans 
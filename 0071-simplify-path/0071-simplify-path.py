class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split('/')
        # print(path.split('/'))
        for p in path:
            if p and p != '.':
                if stack and p == '..':
                    stack.pop()
                elif p != '..':
                    stack.append(p)
            
        return  '/' + '/'.join(stack) 
                

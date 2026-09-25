class Solution:
    def braceExpansionII(self, expr: str) -> list[str]:
        stk,rgt = [], [0]*len(expr)
        for i,c in enumerate(expr):
            if   c=='{': stk.append(i)
            elif c=='}': rgt[stk.pop()] = i
        def parse(l,r):
            lft,ans = {""}, set()
            while (l:= l+1) < r:
                if  (c:= expr[l]) == ',': ans |= lft;  lft = {""}
                elif c == '{':  
                    lft = {e+s for e,s in product(lft, parse(l,rgt[l]))}
                    l   = rgt[l]
                else: lft = {e+c for e in lft}
            return  ans | lft
        return  sorted(parse(-1,len(expr)))
        
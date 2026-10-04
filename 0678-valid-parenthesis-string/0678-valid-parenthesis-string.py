class Solution:
    def checkValidString(self, s: str) -> bool:
        bMin, bMax=0, 0
        for c in s:
            bMin+=(c=='(')-(c==')')-(c=='*')
            bMax+=(c=='(')-(c==')')+(c=='*')
            if bMax<0: return False
            bMin=max(bMin, 0)
        return bMin==0
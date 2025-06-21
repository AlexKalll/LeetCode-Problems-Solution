class Solution:
    def queryString(self, s: str, n: int) -> bool:
        l=[]
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                l.append(s[i:j])
        for i in range(1,n+1):
            if bin(i)[2:] not in l:
                return False
        return True
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12 or len(s) < 4:
            return []

        ans = []
        def backtrack(i, dots, curr):
            if i == len(s) and dots == 4:
                ans.append(curr[:-1])
                return 
            if dots > 4:
                return 
            
            for j in range(1, 4):
                if i + j <= len(s):  
                    segment = s[i:i+j]
                
                    if (len(segment) == 1) or (segment[0] != '0' and int(segment) <= 255):
                        backtrack(i + j, dots + 1, curr + segment + '.')
                    
            
        backtrack(0, 0, '')

        return ans
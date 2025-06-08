class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []

        def dfs(cur):
            if cur > n:
                return 
            ans.append(cur)
            cur *= 10
            for i in range(10): # not msd
                dfs(cur+i)
            
        for i in range(1,10): # the most segnificat digits 
            dfs(i)
        
        return ans
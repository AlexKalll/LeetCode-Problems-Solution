class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        ans = []

        def backtrack(curr):
            if len(curr) == n:
                ans.append(''.join(curr))
                return 

            for char in 'abc':
                if curr and curr[-1] == char:
                    continue
                curr.append(char)
                backtrack(curr)
                curr.pop()
        
        backtrack([])
        return ans[k-1] if k - 1 < len(ans) else ''
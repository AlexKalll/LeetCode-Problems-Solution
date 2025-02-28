class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:

        n = len(grid[0])
        row_prefix = [[0] * len(grid[0]) for _ in range(2)]
    
        for i in range(2):
            for j in range(n):
                row_prefix[i][j] = (grid[i][j] + (row_prefix[i][j-1] if row_prefix[i][j-1] else 0))
        # print(row_prefix)
        ans = float('inf')
        for i in range(n):
            if i - 1 >= 0:
                curr = max(row_prefix[0][n-1] - row_prefix[0][i], row_prefix[1][i-1])
            else:
                curr = row_prefix[0][n-1] - row_prefix[0][i]

            ans = min(ans, curr)
        
        return ans

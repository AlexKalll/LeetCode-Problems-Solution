class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def inbound(i, j):
            return 0 <= i < n and 0 <= j < m
        

        def dfs(i, j):
            if not inbound(i, j) or not grid[i][j]:
                return False

            area = 1
            grid[i][j] = 0
            for x, y in directions:
                area += dfs(i + x, j + y)
            
            return area
                
        max_area = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    max_area = max(max_area, dfs(i, j))
        
        return max_area
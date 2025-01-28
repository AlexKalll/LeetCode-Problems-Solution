# https://leetcode.com/problems/maximum-number-of-fish-in-a-grid

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]

        def dfs(r: int, c: int) -> int:
            if r < 0 or r >= m or c < 0 or c >= n or visited[r][c] or grid[r][c] == 0:
                return 0
            
            visited[r][c] = True
            fish_count = grid[r][c]
            # Explore adjacent cells
            fish_count += dfs(r + 1, c)  # Down
            fish_count += dfs(r - 1, c)  # Up
            fish_count += dfs(r, c + 1)  # Right
            fish_count += dfs(r, c - 1)  # Left

            return fish_count

        max_fish = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0 and not visited[i][j]:  # Start DFS from each unvisited water cell
                    max_fish = max(max_fish, dfs(i, j))

        return max_fish

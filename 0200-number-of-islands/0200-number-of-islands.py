class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        
        def dfs(row, col):
            visited.add((row, col))
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if (0 <= new_row < rows and 0 <= new_col < cols and
                        (new_row, new_col) not in visited and grid[new_row][new_col] == '1'):
                    dfs(new_row, new_col)

        island_count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    dfs(r, c)
                    island_count += 1

        return island_count

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        perimeter = 0

        def inbound(row, col):
            return 0 <= row < rows and 0 <= col < cols
        
        def dfs(row, col):
            nonlocal perimeter
            visited[row][col] = True
            
            for x, y in directions:
                newr = row + x
                newc = col + y
                
                if inbound(newr, newc):
                    if grid[newr][newc] == 1 and not visited[newr][newc]:  
                        dfs(newr, newc)
                    elif grid[newr][newc] == 0:  
                        perimeter += 1
                else:  # out of bounds (water)
                    perimeter += 1

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    dfs(i, j)
                    break
            else:
                continue

            break
        
        return perimeter 
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        if rows == 0:
            return -1
        cols = len(grid[0])
        queue = deque()
        fresh = 0
        minutes = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        if fresh == 0:
            return 0
        
        while queue:
            minutes += 1
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for di, dj in directions:
                    ni, nj = i + di, j + dj

                    if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == 1:
                        grid[ni][nj] = 2     # Mark as rotten.
                        fresh -= 1
                        queue.append((ni, nj))
                        
            if fresh == 0:
                return minutes
        
        return -1     
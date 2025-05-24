from collections import deque
from typing import List

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        height = [[-1] * n for _ in range(m)]  # Initialize height matrix with -1
        
        # Queue for BFS
        queue = deque()
        
        # Add all water cells to the queue and set their height to 0
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    height[i][j] = 0
                    queue.append((i, j))
        
        # Directions for adjacent cells (up, down, left, right)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # BFS to assign heights
        while queue:
            x, y = queue.popleft()
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                # Check if the new cell is within bounds and is a land cell
                if 0 <= nx < m and 0 <= ny < n and height[nx][ny] == -1:
                    height[nx][ny] = height[x][y] + 1  # Set height
                    queue.append((nx, ny))  # Add to queue for further processing
        
        return height

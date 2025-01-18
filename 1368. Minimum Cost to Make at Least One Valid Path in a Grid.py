# https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/

import heapq
from typing import List

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # Directions corresponding to the signs
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right, left, down, up
        # Cost matrix to track minimum cost to reach each cell
        cost = [[float('inf')] * n for _ in range(m)]
        cost[0][0] = 0
        
        # Priority queue for Dijkstra's algorithm (cost, x, y)
        pq = [(0, 0, 0)]  # (cost, row, column)
        
        while pq:
            current_cost, x, y = heapq.heappop(pq)
            
            # If we reach the bottom-right cell, return the cost
            if x == m - 1 and y == n - 1:
                return current_cost
            
            # If the cost is greater than the recorded cost, skip
            if current_cost > cost[x][y]:
                continue
            
            # Determine the next cell based on the current sign
            direction = grid[x][y] - 1  # Convert to zero-based index
            next_x, next_y = x + directions[direction][0], y + directions[direction][1]
            
            # If the next cell is within bounds, move there without cost
            if 0 <= next_x < m and 0 <= next_y < n:
                if current_cost < cost[next_x][next_y]:
                    cost[next_x][next_y] = current_cost
                    heapq.heappush(pq, (current_cost, next_x, next_y))
            
            # Check all possible directions to modify the sign
            for i in range(4):
                if i != direction:  # Only consider changing the direction
                    next_x, next_y = x + directions[i][0], y + directions[i][1]
                    if 0 <= next_x < m and 0 <= next_y < n:
                        new_cost = current_cost + 1
                        if new_cost < cost[next_x][next_y]:
                            cost[next_x][next_y] = new_cost
                            heapq.heappush(pq, (new_cost, next_x, next_y))
        
        return cost[m - 1][n - 1]

# Example usage:
# grid = [[1,3,4],[2,1,2],[3,4,1]]
# solution = Solution()
# print(solution.minCost(grid))  # Outputs the minimum cost to create a valid path

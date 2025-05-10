class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        values = []
        n = len(grid)
        for i in range(n):
            grid[i].sort(reverse=True)
            for j in range(min(len(grid[i]), limits[i])):
                values.append(grid[i][j])
        values.sort(reverse=True)
        
        max_cum = 0
        for i in range(min(k, len(values))):
            max_cum += values[i]
        
        return max_cum

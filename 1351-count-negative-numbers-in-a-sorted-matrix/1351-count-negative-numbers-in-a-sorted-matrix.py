
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        count = 0
        row, col = m - 1, 0  # Start from the bottom-left corner

        while row >= 0 and col < n:
            if grid[row][col] < 0:
                count += n - col  # All elements to the right are negative
                row -= 1  # Move up
            else:
                col += 1  # Move right

        return count

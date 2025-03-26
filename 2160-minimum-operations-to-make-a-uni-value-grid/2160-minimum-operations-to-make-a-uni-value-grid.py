class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # Flatten the grid
        flat_grid = [num for row in grid for num in row]
        
        # Check if all elements have the same remainder when divided by x
        remainder = flat_grid[0] % x
        for num in flat_grid:
            if num % x != remainder:
                return -1
        
        # Normalize the values by dividing by x
        normalized_grid = [num // x for num in flat_grid]
        
        # Find the median
        median = int(statistics.median(normalized_grid))
        
        # Calculate total operations to convert all to the median
        operations = sum(abs(num - median) for num in normalized_grid)
        
        return operations
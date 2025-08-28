from collections import defaultdict
class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        diagonals_map = defaultdict(list)
        for r in range(n):
            for c in range(n):
                diag_key = r - c
                diagonals_map[diag_key].append(grid[r][c])
        
        sorted_diagonals = {}
        for diag_key, elements in diagonals_map.items():
            if diag_key >= 0:
                elements.sort(reverse=True)
            else:
                elements.sort()
            
            sorted_diagonals[diag_key] = iter(elements)
        
        result_grid = [[0]*n for _ in range(n)]

        for r in range(n):
            for c in range(n):
                diag_key = r - c
                result_grid[r][c] = next(sorted_diagonals[diag_key])
            
        return result_grid

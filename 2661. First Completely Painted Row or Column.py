# https://leetcode.com/problems/first-completely-painted-row-or-column/

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        
        # Create a mapping from value to its position in the matrix
        pos = {}
        for i in range(m):
            for j in range(n):
                pos[mat[i][j]] = (i, j)
        
        # Track the count of painted cells in each row and column
        row_count = [0] * m
        col_count = [0] * n
        
        # Iterate through arr and paint cells
        for index, value in enumerate(arr):
            if value in pos:
                row, col = pos[value]
                row_count[row] += 1
                col_count[col] += 1
                
                # Check if the row or column is completely painted
                if row_count[row] == n or col_count[col] == m:
                    return index
        
        return -1  # In case no complete row or column is found

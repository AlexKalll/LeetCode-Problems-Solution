class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n//2):
            for j in range(n):
                # Swap the top and bottom elements in the column
                matrix[i][j], matrix[n - i-1][j] = matrix[n - i - 1][j], matrix[i][j]
        
        for i in range(n):
            for j in range(i):
                # Swap the elements across the diagonal after doing the above
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
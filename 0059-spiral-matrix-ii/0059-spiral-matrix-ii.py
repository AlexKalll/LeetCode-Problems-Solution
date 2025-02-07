class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        def inbound(i, j):
            return 0 <= i < n and 0 <= j <n

        matrix = [[0]*n for _ in range(n)]
        direct = [(0, 1), (1, 0), (0, -1), (-1, 0)] # the four possible direction moves 

        row = col =dir_idx = 0
        for val in range(1, n*n + 1):
            matrix[row][col] = val

            next_row, next_col = row + direct[dir_idx][0], col + direct[dir_idx][1]

            if not inbound(next_row, next_col) or matrix[next_row][next_col]:
                dir_idx = (dir_idx + 1) % 4

            row, col = row + direct[dir_idx][0], col + direct[dir_idx][1]

        return matrix
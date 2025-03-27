class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        
        # check if possible to place Q in (row, col)
        def can_draw(row, col):
            for i in range(row):
                # check for the column
                if board[i][col] == 'Q':
                    return False
                # check for the diagonals
                if col - (row - i) >= 0 and board[i][col - (row - i)] == 'Q':
                    return False
                if col + (row - i) < n and board[i][col + (row - i)] == 'Q':
                    return False

            return True

        def backtrack(row):
            if row == n:
                ans.append([''.join(curr_row) for curr_row in board])
                return
            
            for col in range(n):
                if not can_draw(row, col):
                    continue
                    
                board[row][col] = 'Q'
                backtrack(row + 1)      
                board[row][col] = '.'

        board = [['.' for _ in range(n)] for _ in range(n)]
        backtrack(0)

        return ans

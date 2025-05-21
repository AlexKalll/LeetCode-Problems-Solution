class Solution:
    def get_neighbors(self, row, col, board, m, n):
        count = 0 
        neighbors = []
        array = [[1, 0], [-1, 0], [0, 1], [0, -1], [1,1], [1, -1], [-1, 1], [-1, -1]]

        for r, c in array:
            if row+r < m and row+r >= 0 and col+c < n and col+c >=0:
                if board[row+r][col+c] == 'E': neighbors.append([row+r, col+c])
                if board[row+r][col+c] == 'M': count += 1

        return count, neighbors               
            

    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m = len(board)
        n = len(board[0])

        queue = deque()
        queue.append(click)        

        while(queue):
            row, col = queue.popleft()
            if board[row][col] == 'M':
                board[row][col] = 'X'
                return board 
            
            if board[row][col] == 'E':
                count, neighbors = self.get_neighbors(row, col, board, m, n)
                
                if count > 0:
                    board[row][col] = str(count) 
                else:
                    board[row][col] = 'B'
                    for r, c in neighbors:   
                        #if board[r][c] == 'E':             
                        queue.append([r, c])
            

        return board
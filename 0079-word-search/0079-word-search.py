class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return False
        
        rows, cols = len(board), len(board[0])
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def in_bounds(r, c):
            return 0 <= r < rows and 0 <= c < cols
        
        def dfs(r, c, index):
            if index == len(word):
                return True
            
            if not in_bounds(r, c) or board[r][c] != word[index]:
                return False
            
            temp = board[r][c]
            board[r][c] = '#'
            
            found = False
            for dr, dc in directions:
                found = found or dfs(r + dr, c + dc, index + 1)
            
            board[r][c] = temp
            
            return found
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        
        return False
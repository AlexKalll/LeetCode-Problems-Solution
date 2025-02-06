class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            cnt = Counter(row)

            for num in cnt:
                if cnt[num] > 1 and num.isdigit():
                    return False
                
        for col in list(zip(*board)):
            cnt = Counter(col)
            for num in cnt:
                if cnt[num] > 1 and num.isdigit():
                    return False
        
        subrow = [(0,2), (3,5), (6,8)]
        subcol = [(0,2), (3,5), (6,8)] 
        for a, b in subrow:    
                for x, y in subcol:
                    hT = defaultdict(int)
                    for i in range(a, b+1):
                        for j in range(x, y+1):
                            if board[i][j] != '.':
                                hT[board[i][j]] += 1
                                
                    for num in hT:
                        if hT[num] >= 2:
                            return False

        return True
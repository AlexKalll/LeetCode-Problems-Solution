class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        
        # self.pref = [[0] * (len(matrix[0]) + 1)]
        # for _ in range(len(matrix) + 1):
        #     self.pref.append([0])
        
        # for i in range(1, len(self.pref)):
        #     for j in range(1, len(self.pref[0])):
        #         self.pref[i][j] = self.matrix[i-1][j-1] + self.pref[i-1][j] + self.pref[i][j-1] - self.pref[i-1][j-1]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i - 1 >= 0 and j - 1 >= 0:
                    self.matrix[i][j] = self.matrix[i][j] + self.matrix[i-1][j] + self.matrix[i][j-1] - self.matrix[i-1][j-1]
                elif i - 1 >= 0:
                    self.matrix[i][j] = self.matrix[i][j] + self.matrix[i-1][j] 
                elif j - 1 >= 0:
                    self.matrix[i][j] = self.matrix[i][j] + self.matrix[i][j-1] 
                else:
                    self.matrix[i][j] = self.matrix[i][j]
                
        print(self.matrix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        if row1 - 1 >= 0 and col1 - 1 >= 0:
            return self.matrix[row2][col2] - self.matrix[row1-1][col2] - self.matrix[row2][col1-1] + self.matrix[row1-1][col1 - 1]
        elif row1 - 1 >= 0:
            return self.matrix[row2][col2] - self.matrix[row1-1][col2] 

        elif col1 - 1 >= 0:
            return self.matrix[row2][col2] - self.matrix[row2][col1-1]
        else:
            return self.matrix[row2][col2] 

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
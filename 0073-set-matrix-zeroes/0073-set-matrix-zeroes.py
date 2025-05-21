class Solution:
    def setZeroes(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m=len(mat)
        n=len(mat[0])
        row=[0]*m
        col=[0]*n
        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                  row[i]=1
                  col[j]=1
        for i in range(m):
            for j in range(n):
                if row[i] or col[j]:
                    mat[i][j]=0
        
        
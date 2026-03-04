class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        row_one_count = []
        col_one_count = []

        for i in range(len(mat)):
            one_count = 0
            for j in range(len(mat[0])):
                if(mat[i][j] == 1):
                    one_count += 1

            row_one_count.append(one_count)

        for j in range(len(mat[0])):
            one_count = 0
            for i in range(len(mat)):
                if(mat[i][j] == 1):
                    one_count += 1
            col_one_count.append(one_count)
        
        count = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):

                if(mat[i][j] == 1):

                    if(row_one_count[i] == 1 and col_one_count[j] == 1):
                        count += 1
                        
        return count
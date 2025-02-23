class Solution:
    def numSubmatrixSumTarget(self, matrix, target):
        if not matrix or not matrix[0]:
            return 0
        
        rows, cols = len(matrix), len(matrix[0])
        prefix_sum = [[0] * (cols + 1) for _ in range(rows + 1)]
        
        for r in range(1, rows + 1):
            for c in range(1, cols + 1):
                prefix_sum[r][c] = (matrix[r-1][c-1] + 
                                    prefix_sum[r-1][c] + 
                                    prefix_sum[r][c-1] - 
                                    prefix_sum[r-1][c-1])
        
        count = 0
        
        for r1 in range(1, rows + 1):
            for r2 in range(r1, rows + 1):
                sum_count = {0: 1}
                current_sum = 0
                
                for c in range(1, cols + 1):
                    current_sum = (prefix_sum[r2][c] - prefix_sum[r1-1][c])
                    count += sum_count.get(current_sum - target, 0)
                    sum_count[current_sum] = sum_count.get(current_sum, 0) + 1
        
        return count
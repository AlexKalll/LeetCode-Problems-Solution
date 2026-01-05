class Solution(object):
    def maxMatrixSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        minAbsValue = float('inf')
        absSum = 0
        negatives = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]<=0:
                    absSum += (-1*matrix[i][j])
                    negatives += 1
                    minAbsValue = min(minAbsValue, (-1*matrix[i][j]))
                else:
                    absSum += matrix[i][j]
                    minAbsValue = min(minAbsValue, matrix[i][j])
        if negatives%2 == 0:
            return absSum
        else:
            return absSum - (2*minAbsValue)
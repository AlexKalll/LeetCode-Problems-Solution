class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        while matrix:
            result += matrix.pop(0)  # pop the first row each time
            matrix = list(zip(*matrix))[::-1] # left rotate matrix 90 degree each time
        return result
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:

        if mat == target:
            return True

        def rotate(matrix):
            # Rotate the matrix 90 deg clockwise
            return [list(row) for row in zip(*matrix)][::-1]
            
        # checking for all four rotations
        for _ in range(3):
            mat = rotate(mat)
            if mat == target:
                return True

        return False

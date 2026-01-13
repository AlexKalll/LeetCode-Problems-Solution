class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        n = len(squares)
        total_area = 0.0
        min_y = float('inf')
        max_y = float('-inf')

        for s in squares:
            curr_y = s[1]
            length = s[2]
            total_area += float(length * length)
            min_y = min(min_y, curr_y)
            max_y = max(max_y, curr_y + length)

        half_area = total_area / 2.0
# # Binary search for the minimum height such that areaBelow(height) >= target.
        for _ in range(100):
            height = (min_y + max_y) / 2.0
            area_below = 0.0

            for s in squares:
                y = s[1]
                length = s[2]
                top_y = y + length

                if height <= y:
                    continue # nothing to add to the area_below
                elif height >= top_y:
                    area_below += length * length
                else: # if height is in b/n y and top_y
                    area_below += (height - y) * length

            if area_below < half_area:
                min_y = height
            else:
                max_y = height

        return max_y
                   
class Solution:
    def checkValidCuts(self, n: int, rectangles: list[list[int]]) -> bool:
        
        def _check_cuts(rectangles, dim):
            gap_count = 0

            # Sort rectangles based on the specified dimension (0 for x, 1 for y)
            rectangles.sort(key=lambda rect: rect[dim])

            # Initialize furthest end based on the first rectangle
            furthest_end = rectangles[0][dim + 2]

            for rect in rectangles[1:]:
                # Check for gaps between rectangles
                if furthest_end <= rect[dim]:
                    gap_count += 1

                # Update the furthest end
                furthest_end = max(furthest_end, rect[dim + 2])

            return gap_count >= 2

        # Check both dimensions: horizontal (y) and vertical (x)
        return _check_cuts(rectangles, 0) or _check_cuts(rectangles, 1)

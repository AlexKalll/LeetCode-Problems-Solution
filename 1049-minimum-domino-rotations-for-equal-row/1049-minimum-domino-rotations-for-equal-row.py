class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def check(candidate: int) -> int:
            rotations_top = rotations_bottom = 0
            for t, b in zip(tops, bottoms):
                if t != candidate and b != candidate:
                    return float('inf')  # Cannot make this candidate work
                elif t != candidate:
                    rotations_top += 1  # Need to rotate this domino
                elif b != candidate:
                    rotations_bottom += 1  # Need to rotate this domino
            return min(rotations_top, rotations_bottom)

        # Check both candidates
        candidate1 = tops[0]
        candidate2 = bottoms[0]
        
        rotations1 = check(candidate1)
        rotations2 = check(candidate2)
        
        result = min(rotations1, rotations2)
        
        return result if result != float('inf') else -1
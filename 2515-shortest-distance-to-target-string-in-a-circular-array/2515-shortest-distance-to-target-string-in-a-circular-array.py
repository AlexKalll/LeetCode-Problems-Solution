class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        min_dist = float('inf')

        for i, word in enumerate(words):
            if word == target:
                forward_dist = abs(i - startIndex)
                backward_dist = n - forward_dist
                min_dist = min(min_dist, forward_dist, backward_dist)

        return -1 if min_dist == float('inf') else min_dist
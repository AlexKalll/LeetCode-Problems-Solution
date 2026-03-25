class Solution:
    def canPartitionGrid(self, g: List[List[int]]) -> bool:
        return any(q[-1]/2 in q for q in ([*accumulate(map(sum,g))] for g in (g,zip(*g))))
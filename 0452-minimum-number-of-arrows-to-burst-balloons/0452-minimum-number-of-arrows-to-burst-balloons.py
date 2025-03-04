class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        n = len(points)
        points.sort(key = lambda x: x[1])
        count = 0
        i = 0
        
        while i < n:
            j = i + 1
            while j < n and points[j][0] <= points[i][1]:
                j += 1
            
            i = j
            count += 1

        return count


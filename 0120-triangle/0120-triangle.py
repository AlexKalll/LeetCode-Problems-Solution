class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        path = triangle.pop(0)
        while triangle:
            level = triangle.pop(0)
            for i in range(len(level)):
                if i-1 >= 0 and i+1 <= len(path):
                    level[i] += min(path[i-1], path[i])
                elif i-1 < 0:
                    level[i] += path[i]
                elif i+1 >= len(path):
                    level[i] += path[i-1]
            path = level
        return min(path) 
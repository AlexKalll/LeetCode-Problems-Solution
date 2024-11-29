class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def sorter(x):
            a, b = x
            distance = a**2 + b**2
            return distance 
        # the above code is equivalent to -> sorter = lambda x: x[0]**2 + x[1]**2
        points.sort(key = sorter) # or simply -> points.sort(key = lambda x: x[0]**2 + x[1]**2)

        return points[:k]

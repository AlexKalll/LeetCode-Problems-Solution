class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 1:
            return 0
        
        cost = 0
        visited = [False] * n
        min_heap = [(0, 0)]  
        
        while min_heap:
            c, u = heapq.heappop(min_heap)
            if visited[u]:
                continue
            visited[u] = True
            cost += c
            
            for v in range(n):
                if not visited[v]:
                    d = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                    heapq.heappush(min_heap, (d, v))
        
        return cost
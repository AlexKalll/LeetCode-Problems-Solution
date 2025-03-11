class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u,v,w in edges:
            graph[u].append((v,w))
            graph[v].append((u,w))

        dist = [float('inf')]*(n+1) #Dijkstra array to store shortest path
        dist[n] = 0
        MOD = 10**9 + 7

        dp = [0]*(n+1)
        dp[n] = 1 #base case: 1 way for last node to itself

        #update from last node -> 1
        pq = [(0, n)]
        while pq:
            dis, node = heapq.heappop(pq)

            if dis > dist[node]:
                continue
            
            for nei, w in graph[node]:
                new_dis = dis + w
                if new_dis < dist[nei]:
                    dist[nei] = new_dis
                    heapq.heappush(pq, (new_dis, nei))
                    
                #current path distance > shortest path to neighbor, update dp
                elif dis > dist[nei]: 
                    dp[node] = (dp[node] + dp[nei]) % MOD
            
            if node == 1:
                break

        return dp[1]
        
class Solution:
    def shortestAlternatingPaths(self, n: int, r: List[List[int]], b: List[List[int]]) -> List[int]:
        r_adj = [[] for _ in range(n)]
        b_adj = [[] for _ in range(n)]
        
        for u, v in r:
            r_adj[u].append(v)
        for u, v in b:
            b_adj[u].append(v)
        
        q = deque()
        res = [[float('inf'), float('inf')] for _ in range(n)]
        res[0] = [0, 0]
        
        q.append((0, -1))  
        q.append((0, 1))   
        
        curr_dist = 0
        while q:
            for _ in range(len(q)):
                node, edge_color = q.popleft()
                
                if edge_color == 1: 
                    for next_node in r_adj[node]:
                        if res[next_node][1] > curr_dist + 1:
                            q.append((next_node, -1))
                            res[next_node][1] = curr_dist + 1
                else:  
                    for next_node in b_adj[node]:
                        if res[next_node][0] > curr_dist + 1:
                            q.append((next_node, 1))
                            res[next_node][0] = curr_dist + 1
            
            curr_dist += 1
        
        ans = []
        for i in range(n):
            min_dist = min(res[i])
            ans.append(-1 if min_dist == float('inf') else min_dist)
        
        return ans
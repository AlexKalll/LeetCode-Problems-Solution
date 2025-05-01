class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        q = deque()
        for i in range(n):
            if len(graph[i]) == 1:
                q.append(i)
        
        rem = n  
        while rem > 2:
            size = len(q)
            rem -= size
            
            for _ in range(size):
                leaf = q.popleft()
                nei = graph[leaf].pop() 
                graph[nei].remove(leaf) 

                if len(graph[nei]) == 1:
                    q.append(nei)

        return list(q)
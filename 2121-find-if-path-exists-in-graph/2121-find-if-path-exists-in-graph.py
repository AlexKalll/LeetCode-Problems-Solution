class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = [[] for _ in range(n)] 
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # print(graph)
        visited = set()
        def dfs(src, dstn):
            if src == dstn:
                return True

            visited.add(src)
            for nbr in graph[src]:
                if nbr not in visited:
                    if dfs(nbr, dstn):
                        return True

            return False

        return dfs(source, destination)
            
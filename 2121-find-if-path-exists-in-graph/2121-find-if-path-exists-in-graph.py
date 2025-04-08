class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # graph = [[] for _ in range(n)] 
        graph = defaultdict(list)
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # print(graph)
        visited = set()

        def dfs(curr_node):
            if curr_node == destination:
                return True

            visited.add(curr_node)
            for nbr in graph[curr_node]:
                if nbr not in visited:
                    if dfs(nbr):
                        return True

            return False

        return dfs(source)
            
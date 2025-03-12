class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # Topological sorting
        adj_list = [[] for _ in range(n)]
        indegree = [0 for _ in range(n)]
        
        for start, to in edges:
            adj_list[start].append(to)
            indegree[to] += 1

        zero_indegree_nodes = [i for i in range(n) if indegree[i] == 0]
        topological = []
        
        while zero_indegree_nodes:
            curr = zero_indegree_nodes.pop()
            topological.append(curr)

            for nbr in adj_list[curr]:
                indegree[nbr] -= 1
                if indegree[nbr] == 0:
                    zero_indegree_nodes.append(nbr)
        
        ancestors = [[] for _ in range(n)]
        ance_set = [set() for _ in range(n)]
        
        for node in topological:
            for nbr in adj_list[node]:
                ance_set[nbr].add(node)
                ance_set[nbr].update(ance_set[node])

        for i in range(n):
            ancestors[i] = sorted(ance_set[i])  # Store sorted ancestors for each node
        
        return ancestors

# https://leetcode.com/problems/find-eventual-safe-states

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        safe = [0] * n  # 0 = unknown, 1 = safe, 2 = unsafe
        visited = [0] * n  # 0 = unvisited, 1 = visiting, 2 = visited

        def dfs(node):
            if visited[node] == 1:  # Cycle detected
                return False
            if visited[node] == 2:  # Already processed
                return safe[node] == 1
            
            visited[node] = 1  # Mark as visiting
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    safe[node] = 2  # Mark as unsafe
                    visited[node] = 2  # Mark as visited
                    return False

            safe[node] = 1  # Mark as safe
            visited[node] = 2  # Mark as visited
            return True

        for i in range(n):
            if visited[i] == 0:
                dfs(i)

        return [i for i in range(n) if safe[i] == 1]

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = defaultdict(list)

        for a, b in richer:
            graph[b].append(a)
        
        ans = [-1] * n
        
        def dfs(node):
            if ans[node] != -1:
                return ans[node]
            
            ans[node] = node
            
            for richer in graph[node]:
                cand = dfs(richer)
                
                if quiet[cand] < quiet[ans[node]]:
                    ans[node] = cand
            
            return ans[node]
        
        for i in range(n):
            if ans[i] == -1:
                dfs(i)
        
        return ans

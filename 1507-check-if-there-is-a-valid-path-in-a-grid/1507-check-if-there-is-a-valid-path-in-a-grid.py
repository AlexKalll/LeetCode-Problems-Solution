class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        rows, cols = len(grid), len(grid[0])
        drs = {1: [(0, -1), (0, 1)], 2: [(1, 0), (-1, 0)], 3: [(0, -1), (1, 0)],
               4: [(0, 1), (1, 0)], 5: [(0, -1), (-1, 0)], 6: [(0, 1), (-1, 0)]}
        dsu = UnionFind(rows * cols)

        for r in range(rows):
            for c in range(cols):
                for dx, dy in drs[grid[r][c]]:
                    nr, nc = r + dx, c + dy
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if (-dx, -dy) in drs[grid[nr][nc]]:
                            dsu.union(r * cols + c, nr * cols + nc)

        return dsu.find(0) == dsu.find((rows - 1) * cols + (cols - 1))

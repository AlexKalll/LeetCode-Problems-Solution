class Solution:
    def dfs(self, r, c, dir, vis, mp):
        n = len(vis)
        m = len(vis[0])

        if r < 0 or c < 0 or r >= n or c >= m:
            return
        if (r, c) in mp:
            return

        vis[r][c] = 1

        if dir == "r":
            self.dfs(r, c + 1, "r", vis, mp)
        if dir == "l":
            self.dfs(r, c - 1, "l", vis, mp)
        if dir == "u":
            self.dfs(r - 1, c, "u", vis, mp)
        if dir == "d":
            self.dfs(r + 1, c, "d", vis, mp)

    def countUnguarded(self, m, n, guards, walls):
        vis = [[0] * n for _ in range(m)]
        mp = {}

        for x, y in guards:
            mp[(x, y)] = 1
            vis[x][y] = 1

        for x, y in walls:
            mp[(x, y)] = 1
            vis[x][y] = 1

        for x, y in guards:
            self.dfs(x, y + 1, "r", vis, mp)
            self.dfs(x, y - 1, "l", vis, mp)
            self.dfs(x + 1, y, "d", vis, mp)
            self.dfs(x - 1, y, "u", vis, mp)

        return sum(vis[i][j] == 0 for i in range(m) for j in range(n))
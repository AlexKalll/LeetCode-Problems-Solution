class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1          # number of distinct values
        if n == 1:
            return m % MOD

        up = [0] * m
        down = [0] * m
        
        for v in range(m):
            up[v] = v
            down[v] = m - 1 - v


        for _ in range(3, n + 1):
            
            pref_down = [0] * m
            pref_down[0] = down[0] % MOD
            for i in range(1, m):
                pref_down[i] = (pref_down[i - 1] + down[i]) % MOD

            
            suff_up = [0] * m
            suff_up[m - 1] = up[m - 1] % MOD
            for i in range(m - 2, -1, -1):
                suff_up[i] = (suff_up[i + 1] + up[i]) % MOD

            new_up = [0] * m
            new_down = [0] * m
            for v in range(m):
                # new_up[v] = sum of down[w] for w < v
                new_up[v] = pref_down[v - 1] if v > 0 else 0
                # new_down[v] = sum of up[w] for w > v
                new_down[v] = suff_up[v + 1] if v < m - 1 else 0
            up, down = new_up, new_down

        return (sum(up) + sum(down)) % MOD
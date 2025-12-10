class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        n = len(complexity)
        mod = 10**9 + 7
        for i in range(1, n):
            if complexity[i] <= complexity[0]:
                return 0
        res = 1
        for i in range(1, n):
            res = (res * i) % mod
        return res
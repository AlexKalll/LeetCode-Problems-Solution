class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        roots = [ _ for _ in range(26)]
        def get_index(c):
            return ord(c) - 97
        def find(x):
            
            if roots[x] != x:
                roots[x] = find(roots[x])
            return roots[x]
        def union(x,y):
            X, Y = find(x), find(y)
            if X == Y:
                return
            roots[Y] = X


        for u, n, e, v in equations:
            if n == "=":
                union(get_index(u),get_index(v))
        for u, n, e, v in equations:
            if n == "!":
                U, V = find(get_index(u)), find (get_index(v))
                if U == V:
                    return False
        return True
        
class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        m = dict(zip(chars, vals))
        res = cur = 0
        for c in s:
            cur = max(cur + m.get(c, ord(c) - ord('a') + 1), 0)
            res = max(res, cur)
        return res
        
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        tcnt = Counter(t)
        scnt = Counter(s)

        count = 0
        for c in tcnt:
            if tcnt[c] > scnt[c]:
                count += (tcnt[c] - scnt[c])

        return count

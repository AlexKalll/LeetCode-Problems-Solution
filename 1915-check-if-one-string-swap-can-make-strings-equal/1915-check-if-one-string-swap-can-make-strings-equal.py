class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        count = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count += 1
                if count == 1:
                    j = i
                elif count == 2:
                    k = i
        if count == 2:
            s1 = list(s1)
            s1[j], s1[k] = s1[k], s1[j]

        return ''.join(s1) == s2
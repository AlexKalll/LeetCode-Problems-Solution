class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        def find_lcs(s1, s2):  # finding longest common subsequence
            l1, l2 = len(s1), len(s2)

            dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]
            for i in range(1, l1 + 1):
                for j in range(1, l2 + 1):
                    if s1[i - 1] == s2[j - 1]:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                    else:
                        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

            i, j = l1, l2
            lcs = ''

            while i > 0 and j > 0:
                if s1[i - 1] == s2[j - 1]:
                    lcs += s1[i - 1]
                    i -= 1
                    j -= 1
                elif dp[i - 1][j] > dp[i][j - 1]:
                    i -= 1
                else:
                    j -= 1

            return lcs[::-1]  # Reverse the LCS since we built it backwards

        lcs = find_lcs(str1, str2)

        p1 = p2 = 0
        scs = ''

        for char in lcs:
            while p1 < len(str1) and str1[p1] != char:
                scs += str1[p1]
                p1 += 1
            while p2 < len(str2) and str2[p2] != char:
                scs += str2[p2]
                p2 += 1
            
            scs += char
            p1 += 1
            p2 += 1

        # Add any remaining characters from str1 or str2
        scs += str1[p1:] + str2[p2:]

        return scs

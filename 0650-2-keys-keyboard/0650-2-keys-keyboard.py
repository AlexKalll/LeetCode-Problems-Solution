class Solution:
    def minSteps(self, n: int) -> int:
        dp = [0] * (n+1)

        for i in range(2, n+1):
            dp[i] = float("inf")

            for j in range(1, int(i**0.5)+1):
                if i % j == 0:
                    dp[i] = min(dp[i], dp[j] + (i //j))
                    if j != i // j:
                        dp[i] = min(dp[i], dp[i // j] + j)

        return dp[n]
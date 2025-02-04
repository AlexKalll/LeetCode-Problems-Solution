class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest = 0
        for i in range(len(accounts)):
            current = sum(accounts[i])
            richest = max(richest, current)

        return richest

        # time: O(n*m)
        # space: O(1)
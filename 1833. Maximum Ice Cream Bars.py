class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        res = 0
        for c in costs:
            if c <= coins:
                coins -= c
                res+=1
        else:
            return res

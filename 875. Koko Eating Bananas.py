class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours(piles, mid):
            hrs = 0
            for p in piles:
                hrs += math.ceil(p/mid)
            return hrs 
        
        l, r = 1, max(piles)
        ans = r
        while l <= r:
            k = (l + r)//2
            cur = hours(piles, k)
            if cur <= h:
                ans = min(ans, k)
                r = k - 1
            else:
                l = k + 1

        return ans 

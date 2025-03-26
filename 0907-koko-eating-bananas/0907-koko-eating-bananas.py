class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def can_eat(curr_k):
            count = 0
    
            for pile in piles:
                count += (pile // curr_k)
                if pile % curr_k:
                    count += 1

            return count <= h

        low = 1
        high = max(piles)

        while low <= high:
            mid = (low + high) // 2

            if can_eat(mid):
                high = mid - 1
            else:
                low = mid + 1
        
        return low
            
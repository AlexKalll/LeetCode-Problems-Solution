class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        n = len(candies)
        left, right = 1, max(candies)
        result = 0
        
        while left <= right:
            mid = (left + right) // 2
            count = sum(candy // mid for candy in candies)

            if count >= k:
                result = mid  
                left = mid + 1  
            else:
                right = mid - 1 

        return result

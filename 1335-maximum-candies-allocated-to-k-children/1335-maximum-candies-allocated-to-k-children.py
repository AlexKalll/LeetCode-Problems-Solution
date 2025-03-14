class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        left, right = 1, max(candies)
        result = 0
        
        while left <= right:
            mid = (left + right) // 2
            count = sum(candy // mid for candy in candies)

            if count >= k:
                result = mid  # We can satisfy at least k children
                left = mid + 1  # Try for a larger number of candies
            else:
                right = mid - 1  # Try for a smaller number of candies

        return result

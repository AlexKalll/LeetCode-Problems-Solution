class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def isPossible(capacity):
            count = 1
            curr_sum = 0
            for num in weights:
                if curr_sum + num <= capacity:
                    curr_sum += num
                else:
                    curr_sum = num
                    count += 1

            return count <= days

        low = max(weights)
        high = sum(weights)

        while low <= high:
            mid = (low + high) // 2

            if isPossible(mid):
                high = mid - 1
            else:
                low = mid + 1

        return low 
            
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def canRepairInTime(T: int) -> bool:
            total_cars_repaired = 0
            for rank in ranks:
                total_cars_repaired += int(math.sqrt(T // rank))
                if total_cars_repaired >= cars:
                    return True
            return total_cars_repaired >= cars

        left, right = 0, max(ranks) * cars * cars  # Set an upper bound
        while left < right:
            mid = (left + right) // 2
            if canRepairInTime(mid):
                right = mid  # Try for a smaller time
            else:
                left = mid + 1  # Increase time

        return left

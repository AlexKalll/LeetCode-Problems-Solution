class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        
        def canRepairInTime(time):
            total_cars_repaired = 0
            for rank in ranks:
                total_cars_repaired += int(math.sqrt(time // rank))
                if total_cars_repaired >= cars:
                    return True
            return total_cars_repaired >= cars

        left, right = 0, max(ranks) * cars * cars  
        while left < right:
            mid = (left + right) // 2
            if canRepairInTime(mid):
                right = mid  
            else:
                left = mid + 1  

        return left

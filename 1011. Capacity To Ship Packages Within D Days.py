class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(capacity):
            total_weight = 0
            days_needed = 1  # Start with one day
            
            for weight in weights:
                total_weight += weight
                if total_weight > capacity:
                    days_needed += 1  # Need a new day
                    total_weight = weight  # Start new day's weight with current package
                    if days_needed > days:  # If we exceed the allowed days, return False
                        return False
            
            return True
        
        l, h = max(weights), sum(weights)  # Set bounds for binary search
        
        while l < h:
            mid = (l + h) // 2
            if canShip(mid):  # Check if we can ship with current capacity
                h = mid  # Try for a smaller capacity
            else:
                l = mid + 1  # Increase capacity
        
        return l  # l will be the minimum capacity that works

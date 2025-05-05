class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        houses.sort()

        def check(m):
            i , j = 0, 0
            while i < len(houses) and j < len(heaters):
                if abs(houses[i] - heaters[j]) <= m:
                    i += 1
                else:
                    j += 1
            return i == len(houses)
                    
                
        left = 0
        right = max(houses[-1],heaters[-1])
        
        while left <= right:
            mid = (left + right) // 2

            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        
        return left
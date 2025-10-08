class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        result = []
        potions.sort()
        
        for s in spells:
            left, right = 0, len(potions) - 1
            index = len(potions)
            
            # Binary search for first potion
            while left <= right:
                mid = (left + right) // 2
                if s * potions[mid] >= success:
                    index=mid
                    right=mid - 1
                else:
                    left=mid + 1
            result.append(len(potions) - index)
        
        return result
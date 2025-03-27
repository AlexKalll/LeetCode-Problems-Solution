from collections import Counter

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        
        ht = Counter(nums)
        dominant = max(ht, key=ht.get)
        dominant_count = ht[dominant]
    
        left_dominant_count = 0
        for i in range(n - 1):  
            if nums[i] == dominant:
                left_dominant_count += 1
            
            if 2 * left_dominant_count > i + 1 and 2 * (dominant_count - left_dominant_count) > (n - i - 1):
                return i
        
        return -1

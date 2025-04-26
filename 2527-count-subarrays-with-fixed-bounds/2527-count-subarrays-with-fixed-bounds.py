class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        n = len(nums) #
        count = 0
        left = 0
        last_minK = -1
        last_maxK = -1
        
        for i in range(n):
            if nums[i] < minK or nums[i] > maxK:
                left = i + 1  
                last_minK = -1
                last_maxK = -1
            if nums[i] == minK:
                last_minK = i
            if nums[i] == maxK:
                last_maxK = i
            
            if last_minK != -1 and last_maxK != -1:
                count += max(0, min(last_minK, last_maxK) - left + 1)
        
        return count

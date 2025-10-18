class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 0
        last_used = -10**18  # some very small number
        
        for x in nums:
            # choose the smallest possible unique number within range
            new_val = max(x - k, last_used + 1)
            if new_val <= x + k:
                count += 1
                last_used = new_val
        
        return count

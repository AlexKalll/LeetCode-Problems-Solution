class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        unique_elements = set(nums)
        unique_count = len(unique_elements)
        n = len(nums)
        count = 0
        
        for start in range(n):
            seen = {}
            for end in range(start, n):
                seen[nums[end]] = seen.get(nums[end], 0) + 1
                if len(seen) == unique_count:
                    count += 1
        
        return count

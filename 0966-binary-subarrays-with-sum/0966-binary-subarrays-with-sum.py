class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        pref_sum = 0
        count = 0
        sum_count = Counter({0 : 1})

        for bit in nums:
            pref_sum += bit
            count += sum_count[pref_sum - goal]
            
            sum_count[pref_sum] += 1
        
        return count

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pref_sum = 0
        mod_count = defaultdict(int)
        mod_count[0] = 1
        count = 0

        for num in nums:
            pref_sum += num 
            mod = pref_sum % k

            count += mod_count[mod]
            mod_count[mod] += 1
        
        return count 
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_count = Counter({0 : 1})
        pref_sum = 0
        ans = 0

        for num in nums:
            pref_sum += num
            ans += sum_count[pref_sum - k]
            sum_count[pref_sum] += 1
            
        return ans 
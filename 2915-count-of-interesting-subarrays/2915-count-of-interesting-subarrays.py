class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        transformed = [1 if num % modulo == k else 0 for num in nums]
        prefix_sum = 0
        count_map = defaultdict(int)
        count_map[0] = 1
        ans = 0
        
        for value in transformed:
            prefix_sum += value
            target = (prefix_sum - k) % modulo
            ans += count_map[target]
            count_map[prefix_sum % modulo] += 1
        
        return ans
class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        left = 0
        count = 0
        pairs = 0
        freq = defaultdict(int)

        for right in range(len(nums)):
            freq[nums[right]] += 1
            pairs += freq[nums[right]] - 1

            while pairs >= k:
                count += len(nums) - right
                freq[nums[left]] -= 1
                pairs -= freq[nums[left]]
                left += 1
        return count
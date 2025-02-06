class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        
        pair_cnt = Counter(nums)
        pair = non_pair = 0
        for num in pair_cnt:
            n = pair_cnt[num]
            pair += n//2
            non_pair += n%2
        
        return [pair, non_pair]
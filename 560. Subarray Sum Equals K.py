class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        # print(count)
        s = 0
        ans = 0
        count[0] = 1
        for val in nums:
            s += val 
            ans += count[s-k]
            count[s] += 1
        # print(count)
        return ans 

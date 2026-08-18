class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ht = defaultdict(int)
        

        for i in range(n - k + 1):
            seen = set()
            for j in range(i, i + k):
                seen.add(nums[j])
            for num in seen:
                ht[num] += 1
      
        ans = -1
        for num, count in ht.items():
            if count == 1:
                ans = max(ans, num)
        
        return ans
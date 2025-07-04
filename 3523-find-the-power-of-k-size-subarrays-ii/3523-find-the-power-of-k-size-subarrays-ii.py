class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        ans, cnt = [], 1
        for i, (x, y) in enumerate(pairwise(nums), 2):
            if x + 1 == y: 
                cnt += 1
            else:
                cnt = 1        
            if i >= k:
                ans.append(y if cnt >= k else -1)
        return ans
        
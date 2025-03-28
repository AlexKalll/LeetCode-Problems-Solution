class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ans = 0
        l = 0
        cnt = 0
        
        for r in range(len(nums)):
            if nums[r] == 0:
                cnt += 1
            while cnt > k :   
                if nums[l] == 0:
                    cnt -= 1
                l += 1   
            
            if cnt == k:
                ans = max(ans, r-l+1)

        return ans

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        cnt=[0]*101
        res=0
        for i in nums:
            cnt[i]+=1
        maxi=max(cnt)
        for i in cnt:
            if i==maxi:
                res+=maxi
        
        return res
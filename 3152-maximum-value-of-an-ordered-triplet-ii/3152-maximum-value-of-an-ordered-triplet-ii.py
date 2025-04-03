class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        max_pref = [0] * (n + 1)
        
        for i in range(n):
            max_pref[i + 1] = max(max_pref[i], nums[i])
        
        max_suff = [0] * (n + 1)
        
        for i in range(n - 1, -1, -1):  
            max_suff[i] = max(max_suff[i + 1], nums[i])

        ans = float('-inf')  

        for i in range(1, n - 1):
            curr = (max_pref[i] - nums[i]) * max_suff[i + 1]  
            ans = max(ans, curr)

        return max(ans, 0)  

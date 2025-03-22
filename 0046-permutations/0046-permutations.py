class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        def backtrack(k, perm, used):
            if len(perm) == len(nums):
                ans.append(perm[:])
                return 
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                perm.append(nums[i])
                backtrack(i, perm, used)
                perm.pop()
                used[i] = False
        
        used = [False] * len(nums)
        backtrack(0, [], used)
        return ans

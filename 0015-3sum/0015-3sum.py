class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        for i in range(len(nums)):
            pre = nums[i]
            l = i + 1
            r = len(nums) - 1
            while l < r:
                val = pre + nums[l] + nums[r]
                if val < 0:
                    l +=1
                elif val > 0:
                    r -= 1
                elif val ==0:
                    ans.add((pre, nums[l], nums[r]))
                    r -=1
                    l += 1
                    
        return list(ans)

# in list it is possible to have set, tuple etc are acceptible as a list finally...
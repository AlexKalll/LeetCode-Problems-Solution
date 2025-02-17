class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_product = 1
        suf_product = 1
        n = len(nums)
        ans = [1] * n

        for i in range(n):
            ans[i] *= pre_product 
            pre_product *= nums[i]
        
        for i in reversed(range(n)):
            ans[i] *= suf_product 
            suf_product *= nums[i]

        return ans
class Solution:
    def minOperations(self, nums, k):
        
        heapify (nums)
        ans  = 0
        x = heappop(nums)
        
        while x < k:
            y = heappop(nums)
            nxt = 2*x + y
            x = heappushpop(nums, nxt) # it pops the smallest num x before pushing nxt
            ans+= 1

        return ans
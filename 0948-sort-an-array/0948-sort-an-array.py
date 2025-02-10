class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        m = min(nums)
        M = max(nums)

        width = M - m + 1
        holder = [0] * width 

        offset = m

        for num in nums:
            holder[num - offset] += 1
        
        ans = []

        for i in range(width):
            ans.extend([i+offset] * holder[i])
            
        return ans 

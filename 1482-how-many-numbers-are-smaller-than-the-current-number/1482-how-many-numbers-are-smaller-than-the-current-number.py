class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # m = 0 # min(nums) but look at the constraints of the problem 
        # M = max(nums)
        # width = M - m + 1
        count_arr = [0] * 101

        for num in nums:
            count_arr[num] += 1
        
        count = count_arr[0]
        count_arr[0] = 0
        
        for i in range(1, 101):
            curr = count_arr[i]
            count_arr[i] = count
            count += curr
        
        ans = []
        
        for num in nums:
            ans.append(count_arr[num])
        
        return ans
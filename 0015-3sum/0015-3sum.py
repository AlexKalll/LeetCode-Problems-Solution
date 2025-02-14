class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        ans = []

        for i in range(len(nums) - 2):
            if i> 0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]

            left = i+ 1
            right = len(nums) - 1
            

            while left < right:
                curr_sum = nums[left] + nums[right]
                if curr_sum > target:
                    right -= 1
                elif curr_sum < target:
                    left += 1
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left +=1


        return ans 
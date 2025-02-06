class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        # applying the operations 
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1] and nums[i] != 0:
                nums[i] *= 2
                nums[i+1] = 0

        # applying two pointers approach to push all zeros to the end
        l  = 0
        print(nums)
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1

        return nums
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]

        return nums

        # It is overitten approach
        # time: O(n)
        # space: O(1)


"""
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = [nums[0]]
        for i in range(1, len(nums)):
            running_sum.append(running_sum[-1] + nums[i])

        return running_sum 
        
        # time complexity: O(n)
        #space complexity: O(n)
        """

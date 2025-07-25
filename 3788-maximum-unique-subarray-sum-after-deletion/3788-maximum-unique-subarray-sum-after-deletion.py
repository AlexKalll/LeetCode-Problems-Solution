class Solution:
    def maxSum(self, nums: List[int]) -> int:
        # Remove duplicates in-place, accumulate positive values, 
        # and track the maximum
        total = 0
        maximum = nums[0]
        i = 0
        
        while i < len(nums):
            current = nums[i]
            # Update maximum value
            if current > maximum:
                maximum = current
            # Add positive values to the total sum
            if current > 0:
                total += current
            
            # Remove all future duplicates of current
            j = i + 1
            while j < len(nums):
                if nums[j] == current:
                    # Swap duplicate with last element and pop
                    nums[j] = nums[-1]
                    nums.pop()
                    # Do not advance j to check the swapped-in element
                else:
                    j += 1
            i += 1
        
        # If the largest value is negative, or larger than 
        # the sum of positives, return it instead of the total
        if maximum < 0 or maximum > total:
            return maximum
        return total
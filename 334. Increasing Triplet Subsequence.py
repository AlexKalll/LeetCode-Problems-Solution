class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        num1 = num2 = float('inf')
        for num3 in nums:
            if num3 <= num1:
                num1 = num3  # Update num1 to the current number
            elif num3 <= num2:
                num2 = num3  # Update num2 to the current number
            else: 
                return True  # Found a valid triplet
                
        return False  # No triplet found

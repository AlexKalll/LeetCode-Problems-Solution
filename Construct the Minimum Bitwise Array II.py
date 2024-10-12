class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = [-1] * len(nums)  # Initialize result list
        
        for i in range(len(nums)):
            Min = 10 ** 9 # in the constraint sectioin it says max nums[i] <= 10^9
            
            for cur in range(100): # Check each bit position from 0 to 99 (assuming 100 bits)
                if (nums[i] >> cur) & 1:  # If cur-th bit is set i.e if it is set(1) in nums[i]
                    pos = nums[i] & ~(1 << cur)  # Flip the cur-th bit to 0

                    if pos < 0:  # Skip if pos is negative
                        continue
                    
                    if (pos | (pos + 1)) == nums[i]:  # Check if valid transformation
                        if pos < Min:  # Update minimum if pos is smaller
                            ans[i] = pos
        
        return ans  # Return the result list

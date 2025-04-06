from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
    
        nums.sort()
        
        n = len(nums)
        dp = [1] * n  # dp[i] will hold the size of the largest divisible subset that ends with nums[i]
        parent = [-1] * n  # To reconstruct the path
        
        max_size = 0
        max_index = 0
        
        # Step 3: Fill the dp array
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        parent[i] = j
            
            # Update the maximum size and index
            if dp[i] > max_size:
                max_size = dp[i]
                max_index = i
        
        # Step 4: Reconstruct the largest divisible subset
        result = []
        while max_index != -1:
            result.append(nums[max_index])
            max_index = parent[max_index]
        
        return result[::-1]  # Reverse to get the correct order

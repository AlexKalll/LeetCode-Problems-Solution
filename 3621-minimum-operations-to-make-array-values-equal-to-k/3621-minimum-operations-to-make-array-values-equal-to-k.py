class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # Check for impossible case
        if any(num < k for num in nums):
            return -1
        
        # Create a set of distinct integers greater than k
        distinct_greater_than_k = {num for num in nums if num > k}
        
        # The number of operations is the size of this set
        return len(distinct_greater_than_k)
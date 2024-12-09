class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        
        # Step 1: Compute the "special" array
        special = [0] * (n - 1)
        for i in range(n - 1):
            special[i] = (nums[i] % 2) != (nums[i + 1] % 2)  # True if adjacent elements have different parity
        
        # Step 2: Compute prefix sum of "non-special" counts
        prefix_count = [0] * n
        for i in range(1, n):
            prefix_count[i] = prefix_count[i - 1] + (0 if special[i - 1] else 1)  # Count non-special pairs
        
        # Step 3: Process the queries
        result = []
        for from_index, to_index in queries:
            if from_index == to_index:  # A single element is always special
                result.append(True)
            else:
                # Check if there are any non-special pairs in the range
                if prefix_count[to_index] - prefix_count[from_index] == 0:
                    result.append(True)
                else:
                    result.append(False)
        
        return result

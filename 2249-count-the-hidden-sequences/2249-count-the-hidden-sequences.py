class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        n = len(differences)
        
        # Step 1: Calculate prefix sums
        prefix_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + differences[i - 1]

        # Step 2: Find min and max of prefix sums
        min_prefix = min(prefix_sum)
        max_prefix = max(prefix_sum)

        # Step 3: Calculate the valid range for the first element of the hidden sequence
        valid_start_min = lower - min_prefix
        valid_start_max = upper - max_prefix
        
        # Step 4: Calculate the number of valid starting points
        return max(0, valid_start_max - valid_start_min + 1)


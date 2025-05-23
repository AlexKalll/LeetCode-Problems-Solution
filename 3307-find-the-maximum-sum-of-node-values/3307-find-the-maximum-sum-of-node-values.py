class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
         # Step 1: Calculate base sum
        base_sum = sum(nums)

        # Step 2: Calculate gains for XORing each number
        gains = [(num ^ k) - num for num in nums]

        # Step 3: Sort gains descending
        gains.sort(reverse=True)

        # Step 4: Choose best even-number gain sum
        max_gain = 0
        current_gain = 0
        count = 0

        for gain in gains:
            current_gain += gain
            count += 1
            # Step 5: Only consider even count of XORs
            if count % 2 == 0:
                max_gain = max(max_gain, current_gain)

        # Step 6: Return final result
        return base_sum + max_gain
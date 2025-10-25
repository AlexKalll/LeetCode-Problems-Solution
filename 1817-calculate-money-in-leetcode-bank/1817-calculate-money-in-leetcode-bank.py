class Solution:
    def totalMoney(self, n: int) -> int:
        full_weeks = n // 7
        remaining_days = n % 7

        # Sum for full weeks
        total = 28 * full_weeks + 7 * (full_weeks - 1) * full_weeks // 2

        # Sum for remaining days
        start = full_weeks + 1
        total += remaining_days * start + (remaining_days - 1) * remaining_days // 2


        return total
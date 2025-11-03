class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total_time = 0
        i = 0
        n = len(colors)

        while i < n:
            j = i
            group_sum = 0
            group_max = 0

            # Process group of same colors
            while j < n and colors[j] == colors[i]:
                group_sum += neededTime[j]
                group_max = max(group_max, neededTime[j])
                j += 1

            # Add cost of removing all except the max
            total_time += group_sum - group_max

            # Move to next group
            i = j

        return total_time
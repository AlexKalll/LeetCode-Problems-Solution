import heapq

class Solution():
    def minTimeToReach(self, moveTime):
        n = len(moveTime)
        m = len(moveTime[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # dp[row][col][parity] = earliest time to reach (row, col) with next move of given parity
        dp = [[[float('inf')] * 2 for _ in range(m)] for _ in range(n)]
        dp[0][0][0] = 0  # Start at (0, 0), at time 0, with parity 0 (next move takes 1s)

        pq = [(0, 0, 0, 0)]  # (time, row, col, parity)

        while pq:
            time, row, col, parity = heapq.heappop(pq)
            if (row, col) == (n - 1, m - 1):
                return time
            if time > dp[row][col][parity]:
                continue
            move_cost = 1 if parity == 0 else 2
            next_parity = 1 - parity
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < n and 0 <= c < m:
                    earliest_start = max(time, moveTime[r][c])
                    arrive_time = earliest_start + move_cost
                    if arrive_time < dp[r][c][next_parity]:
                        dp[r][c][next_parity] = arrive_time
                        heapq.heappush(pq, (arrive_time, r, c, next_parity))

        # return -1  # should never reach here

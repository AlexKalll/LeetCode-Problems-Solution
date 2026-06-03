class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:

        def build(starts, durations):
            rides = sorted(zip(starts, durations))

            s = [st for st, _ in rides]
            d = [dur for _, dur in rides]

            n = len(rides)

            prefix_min_dur = [0] * n
            prefix_min_dur[0] = d[0]
            for i in range(1, n):
                prefix_min_dur[i] = min(prefix_min_dur[i - 1], d[i])

            suffix_min_start_dur = [0] * n
            suffix_min_start_dur[-1] = s[-1] + d[-1]
            for i in range(n - 2, -1, -1):
                suffix_min_start_dur[i] = min(
                    suffix_min_start_dur[i + 1],
                    s[i] + d[i]
                )

            return s, prefix_min_dur, suffix_min_start_dur

        def query(t, starts, prefix_min_dur, suffix_min_start_dur):
            pos = bisect_right(starts, t)
            n = len(starts)

            res = float('inf')

            if pos > 0:
                res = min(res, t + prefix_min_dur[pos - 1])

            if pos < n:
                res = min(res, suffix_min_start_dur[pos])

            return res

        water_data = build(waterStartTime, waterDuration)
        land_data = build(landStartTime, landDuration)

        ans = float('inf')

        # Land -> Water
        for s, d in zip(landStartTime, landDuration):
            ans = min(ans, query(s + d, *water_data))

        # Water -> Land
        for s, d in zip(waterStartTime, waterDuration):
            ans = min(ans, query(s + d, *land_data))

        return ans     
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        # print(meetings)
        end = meetings[0][1]
        start = meetings[0][0]
        ans = start - 1

        for i in range(1, len(meetings)):
            curr_start = meetings[i][0]

            if end < curr_start:
                ans += (curr_start - end - 1)

            end = max(end, meetings[i][1])
        
        ans += days - end

        return ans 

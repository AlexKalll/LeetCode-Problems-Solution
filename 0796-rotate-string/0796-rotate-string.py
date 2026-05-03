class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if goal[0] not in s:
            return False
        idx = s.index(goal[0])
        if s.count(goal[0]) == 1:
            return s[idx:] + s[0:idx] == goal
        elif s.count(goal[0]) > 1:
            pivots = []
            for i, c in enumerate(s):
                if c == goal[0]:
                    pivots.append(i)
            for i in pivots:
                if s[i:] + s[0:i] == goal:
                    return True 
        return False
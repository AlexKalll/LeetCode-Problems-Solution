class Solution:
    def judgeCircle(self, moves: str) -> bool:
        pos = [0, 0]

        for ch in moves:

            if (ch == 'U'):
                pos[1] += 1
            elif (ch == 'D'):
                pos[1] -= 1
            elif (ch == 'R'):
                pos[0] += 1
            else:
                pos[0] -= 1

        if (pos == [0, 0]):
            return True
        else:
            return False
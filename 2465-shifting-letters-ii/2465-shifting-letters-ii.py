class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        pref = [0] * len(s)

        for start, end, d in shifts:
            if d == 0:
                pref[start] -= 1
                if end + 1 < len(pref):
                    pref[end+1] += 1
            else:
                pref[start] += 1
                if end + 1 < len(pref):
                    pref[end+1] -= 1

        for i in range(1, len(pref)):
            pref[i] += pref[i-1]


        s = list(s)
        for i, char in enumerate(s):
            curr = ord(char) + pref[i]
            s[i] = chr((curr - 97)% 26 + 97)

        return ''.join(s)

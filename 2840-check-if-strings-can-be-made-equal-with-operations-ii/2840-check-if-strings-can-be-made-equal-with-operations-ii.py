class Solution: # if-else till death
    def checkStrings(self, s1: str, s2: str) -> bool:
        s1, s2 = list(s1), list(s2)
        counter1 = [dict(), dict()]
        counter2 = [dict(), dict()]
        for i in range(len(s1)):
            if i & 1 == 0:
                if s1[i] in counter1[0]:
                    counter1[0][s1[i]] += 1
                else:
                    counter1[0][s1[i]] = 1
                if s2[i] in counter2[0]:
                    counter2[0][s2[i]] += 1
                else:
                    counter2[0][s2[i]] = 1
            else:
                if s1[i] in counter1[1]:
                    counter1[1][s1[i]] += 1
                else:
                    counter1[1][s1[i]] = 1
                if s2[i] in counter2[1]:
                    counter2[1][s2[i]] += 1
                else:
                    counter2[1][s2[i]] = 1
        return counter1 == counter2
        
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count = defaultdict(int)
        for bill in bills:
            count[bill] += 1
            if bill == 10:
                if count[5]:
                    count[5] -= 1
                else:
                    return False
            if bill == 20:
                if count[10] and count[5]:
                    count[10] -= 1
                    count[5] -= 1
                elif count[5] >= 3:
                    count[5] -= 3
                else:
                    return False

        return True

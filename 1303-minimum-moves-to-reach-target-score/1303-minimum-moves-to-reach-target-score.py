class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count = 0

        while target != 1 and maxDoubles:
            rem = target % 2
            target //= 2
            maxDoubles -= 1
            count += 1 + rem
        
        if target != 1:
            count += target - 1

        return count 
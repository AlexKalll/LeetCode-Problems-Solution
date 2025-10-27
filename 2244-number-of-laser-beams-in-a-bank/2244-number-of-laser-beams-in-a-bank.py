class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev = total = 0
        for row in bank:
            count = row.count('1')
            if count:
                total += prev * count
                prev = count
        return total
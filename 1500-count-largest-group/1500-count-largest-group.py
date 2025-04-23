class Solution:
    def countLargestGroup(self, n: int) -> int:
        d = {}
        
        for num in range(1, n + 1):
            s = sum(int(digit) for digit in str(num))
            d[s] = d.get(s, 0) + 1
        
        max_size = max(d.values())
        return sum(1 for count in d.values() if count == max_size)

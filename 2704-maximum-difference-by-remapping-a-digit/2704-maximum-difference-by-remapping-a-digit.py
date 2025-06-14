class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        max_val, min_val = num, num
        for d1 in '0123456789':
            for d2 in '0123456789':
                if d1 == d2:
                    continue
                new_num = int(s.replace(d1, d2))
                max_val = max(max_val, new_num)
                min_val = min(min_val, new_num)
        return max_val - min_val

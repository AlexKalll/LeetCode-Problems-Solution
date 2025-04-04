class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def backtrack(i, first, second):
            if i == len(num):
                return True
            
            sum_str = str(first + second)
            if not num.startswith(sum_str, i):
                return False
            
            return backtrack(i + len(sum_str), second, first + second)

        n = len(num)
        for j in range(1, n):
            for k in range(j + 1, n):
                first = num[:j]
                second = num[j:k]
                if (len(first) > 1 and first[0] == '0') or (len(second) > 1 and second[0] == '0'):
                    continue
                if backtrack(k, int(first), int(second)):
                    return True
        
        return False

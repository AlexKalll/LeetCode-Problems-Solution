from collections import Counter
class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        def check(n):
            mpp = Counter(str(n))
            for n, f in mpp.items():
                if str(f) != n:
                    return False

            return True

        i = n+1
        while True:
            if check(i):
                return i

            i += 1
            
        return 0
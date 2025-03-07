class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        
        def get_primes(left, n):
            prime = [True] * (n+1)
            d = 2
            while d*d <= n:
                if prime[d]:
                    for i in range(d*d, n + 1, d):
                        prime[i] = False
                d += 1

            primes = []
            for i in range(2, n +1):
                if prime[i] and i >= left:
                    primes.append(i)
            
            return primes

        primes = get_primes(left, right)

        if len(primes) < 2:
            return [-1, -1]

        min_diff = float('inf')
        ans = [primes[0], primes[1]]
        for i in range(1, len(primes)):
            diff = primes[i] - primes[i-1]
            if diff < min_diff:
                min_diff = diff
                ans = [primes[i-1], primes[i]]

        return ans
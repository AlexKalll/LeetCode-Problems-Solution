from collections import defaultdict

class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        result = 0

        # Function to count valid substrings with at least one character appearing at least k times
        def at_least_k(start):
            freq = defaultdict(int)
            count = 0
            for end in range(start, n):
                freq[s[end]] += 1
                # Check if we have a character with frequency >= k
                if freq[s[end]] == k:
                    count += 1
                # If we have at least one character with frequency >= k, count all substrings
                print(freq)
                if count > 0:
                    # All substrings from `start` to `end` are valid
                    return n - end
            return 0

        # Iterate over all possible starting points for substrings
        for start in range(n):
            result += at_least_k(start)

        return result

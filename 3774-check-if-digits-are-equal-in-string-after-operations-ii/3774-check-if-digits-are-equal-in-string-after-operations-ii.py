class Solution:
    def hasSameDigits(self, s: str) -> bool:
        input_str = s  # Store input midway
        n = len(s)
        N = n - 2
        sum_digits_0 = 0
        sum_digits_1 = 0

        for j in range(N + 1):
            binom_coeff = self.binomMod10(N, j)
            sum_digits_0 = (sum_digits_0 + binom_coeff * (ord(s[j]) - ord('0'))) % 10
            sum_digits_1 = (sum_digits_1 + binom_coeff * (ord(s[j + 1]) - ord('0'))) % 10
        return sum_digits_0 == sum_digits_1

    def binomMod10(self, n: int, k: int) -> int:
        binom_mod_2 = self.binomMod2(n, k)
        binom_mod_5 = self.binomMod5(n, k)
        for x in range(10):
            if x % 2 == binom_mod_2 and x % 5 == binom_mod_5:
                return x
        return 0

    def binomMod2(self, n: int, k: int) -> int:
        return 1 if (n & k) == k else 0

    def binomMod5(self, n: int, k: int) -> int:
        binom_table = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 1, 4, 1]]
        result = 1
        while n > 0 or k > 0:
            n_digit = n % 5
            k_digit = k % 5
            if k_digit > n_digit:
                return 0
            result = (result * binom_table[n_digit][k_digit]) % 5
            n //= 5
            k //= 5
        return result
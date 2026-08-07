class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        factors = [
            (0, 0, 0, 0),  # 0
            (0, 0, 0, 0),  # 1
            (1, 0, 0, 0),  # 2
            (0, 1, 0, 0),  # 3
            (2, 0, 0, 0),  # 4
            (0, 0, 1, 0),  # 5
            (1, 1, 0, 0),  # 6
            (0, 0, 0, 1),  # 7
            (3, 0, 0, 0),  # 8
            (0, 2, 0, 0),  # 9
        ]

        # Factor t into 2, 3, 5, 7.
        need = []

        for p in (2, 3, 5, 7):
            count = 0
            while t % p == 0:
                t //= p
                count += 1
            need.append(count)

        if t != 1:
            return "-1"

        need = tuple(need)

        def build(req):
            two, three, five, seven = req

            eights, two = divmod(two, 3)
            nines, three = divmod(three, 2)
            fours, twos = divmod(two, 2)

            threes = three
            sixes = 0

            # 2 * 3 -> 6
            if twos and threes:
                twos = 0
                threes = 0
                sixes = 1

            # 3 * 4 -> 2 * 6, and 26 < 34
            if threes and fours:
                twos = 1
                threes = 0
                fours = 0
                sixes = 1

            return (
                "2" * twos
                + "3" * threes
                + "4" * fours
                + "5" * five
                + "6" * sixes
                + "7" * seven
                + "8" * eights
                + "9" * nines
            )

        n = len(num)
        minimum = build(need)

        # Even n digits are not enough.
        if len(minimum) > n:
            return minimum

        total = [0] * 4
        first_zero = n

        for i, ch in enumerate(num):
            digit = int(ch)

            if digit == 0 and first_zero == n:
                first_zero = i

            for j in range(4):
                total[j] += factors[digit][j]

        # num already works.
        if first_zero == n and all(
            total[j] >= need[j] for j in range(4)
        ):
            return num

        prefix = total[:]

        # Try changing the rightmost possible digit.
        for i in range(n - 1, -1, -1):
            digit = int(num[i])

            # prefix now represents num[:i]
            for j in range(4):
                prefix[j] -= factors[digit][j]

            # Keeping this prefix would preserve an earlier zero.
            if i > first_zero:
                continue

            spaces_after = n - i - 1

            for bigger in range(digit + 1, 10):
                missing = []

                for j in range(4):
                    supplied = prefix[j] + factors[bigger][j]
                    missing.append(max(0, need[j] - supplied))

                suffix = build(tuple(missing))

                if len(suffix) <= spaces_after:
                    ones = spaces_after - len(suffix)

                    return (
                        num[:i]
                        + str(bigger)
                        + "1" * ones
                        + suffix
                    )

        # No n-digit answer works.
        return "1" * (n + 1 - len(minimum)) + minimum
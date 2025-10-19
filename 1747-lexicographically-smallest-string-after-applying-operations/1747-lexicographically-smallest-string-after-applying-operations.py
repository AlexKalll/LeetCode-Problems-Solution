from collections import deque


class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        seen = set()
        dq = deque([s])
        smallest = s


        while dq:
            curr = dq.popleft()
            if curr in seen:
                continue
            seen.add(curr)
            smallest = min(smallest, curr)


            # Operation 1: add 'a' to odd indices
            arr = list(curr)
            for i in range(1, len(arr), 2):
                arr[i] = str((int(arr[i]) + a) % 10)
            added = "".join(arr)


            # Operation 2: rotate right by b
            rotated = curr[-b:] + curr[:-b]


            dq.append(added)
            dq.append(rotated)


        return smallest
class Solution:
    def robotWithString(self, s: str) -> str:
        n = len(s)
        suffix_min = [''] * n
        # Step 1: Build suffix minimum array
        suffix_min[-1] = s[-1]
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(s[i], suffix_min[i + 1])

        stack = []
        result = []

        # Step 2: Simulate stack operations
        for i in range(n):
            # Push current character onto stack
            stack.append(s[i])
            # Pop while top <= smallest future char or at last index
            while stack and (i == n - 1 or stack[-1] <= suffix_min[i + 1]):
                result.append(stack.pop())

        return ''.join(result)
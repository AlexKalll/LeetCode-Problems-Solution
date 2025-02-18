class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        ans, stack = [], []

        for i, char in enumerate(s + "I"):
            stack.append(str(i))

            if char == "I":
                ans += stack[::-1]
                stack = []

        return list(map(int, ans))

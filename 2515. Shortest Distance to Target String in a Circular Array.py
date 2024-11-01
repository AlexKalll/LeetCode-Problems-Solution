class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        # Return -1 if the target is not in the words list
        if target not in words:
            return -1

        def leftward(words, target, i, n):
            leftcnt = 0  # Counter for leftward distance
            while True:
                # Move left in a circular manner
                if words[i] == target:
                    return leftcnt
                i = (i - 1) % n
                leftcnt += 1

        def rightward(words, target, i, n):
            rightcnt = 0  # Counter for rightward distance
            while True:
                # Move right in a circular manner
                if words[i] == target:
                    return rightcnt
                i = (i + 1) % n
                rightcnt += 1

        # Get counts for leftward and rightward distances
        leftcnt = leftward(words, target, startIndex, len(words))
        rightcnt = rightward(words, target, startIndex, len(words))

        # Return the minimum distance found
        return min(leftcnt, rightcnt)

class Solution:
    def stringSequence(self, target: str) -> List[str]:
        result = []
        current = ""

        # Append 'a' to start the sequence
        for i in range(len(target)):
            # Append 'a' to current string
            current += 'a'
            result.append(current)

            # Change the last character to match the target character
            for j in range(ord('a'), ord(target[i]) + 1):
                new_char = chr(j)
                if current[-1] != new_char:  # Only change if it's different
                    current = current[:-1] + new_char
                    result.append(current)

        return result

# https://leetcode.com/problems/shifting-letters-ii/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        # Initialize a difference array
        diff = [0] * (n + 1)

        # Apply the shifts to the difference array
        for start, end, direction in shifts:
            if direction == 1:
                diff[start] += 1  # Start shifting forward
                if end + 1 < n:
                    diff[end + 1] -= 1  # Stop shifting after end
            else:
                diff[start] -= 1  # Start shifting backward
                if end + 1 < n:
                    diff[end + 1] += 1  # Stop shifting after end

        # Calculate the cumulative shifts
        cumulative_shift = 0
        result = []

        for i in range(n):
            cumulative_shift += diff[i]
            # Calculate the new character with wrapping
            new_char = chr((ord(s[i]) - ord('a') + cumulative_shift) % 26 + ord('a'))
            result.append(new_char)

        return ''.join(result)

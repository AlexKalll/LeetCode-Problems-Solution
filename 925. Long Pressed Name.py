# https://leetcode.com/problems/long-pressed-name/
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, j = 0, 0  # Pointers for name and typed strings

        while j < len(typed):
            if i < len(name) and name[i] == typed[j]:
                i += 1  # Move to the next character in name
            elif j == 0 or typed[j] != typed[j - 1]:
                return False  # If current typed character is not the same as the previous one or the first cahrs of name and typed are not same
            j += 1  # Move to the next character in typed

        # Check if all characters in name were matched
        return i == len(name)

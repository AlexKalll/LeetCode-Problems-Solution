# https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/

class Solution:
    def canBeValid(self, s, locked):
        length = len(s)

        # If length of string is odd, return false.
        if length % 2 == 1:
            return False

        open_indices = []
        unlocked_indices = []

        # Iterate through the string to handle '(' and ')'
        for i in range(length):
            if locked[i] == "0":
                unlocked_indices.append(i)
            elif s[i] == "(":
                open_indices.append(i)
            elif s[i] == ")":
                if open_indices:
                    open_indices.pop()  # Match with an opened '('
                elif unlocked_indices:
                    unlocked_indices.pop()  # Use an unlocked position
                else:
                    return False  # No match available

        # Match remaining open brackets with unlocked characters
        while open_indices and unlocked_indices and open_indices[-1] < unlocked_indices[-1]:
            open_indices.pop()
            unlocked_indices.pop()

        # If there are unmatched open brackets left, return false
        if open_indices:
            return False

        return True

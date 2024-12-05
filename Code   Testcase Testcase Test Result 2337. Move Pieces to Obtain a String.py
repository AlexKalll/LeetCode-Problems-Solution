class Solution:
    def canChange(self, start: str, target: str) -> bool:
        # Initialize pointers for both strings and get their length
        i, j, n = 0, 0, len(start)
        
        # Loop until both pointers have traversed their respective strings
        while i < n or j < n:
            # Move pointer i to the next non-blank character in start
            while i < n and start[i] == '_':
                i += 1
            
            # Move pointer j to the next non-blank character in target
            while j < n and target[j] == '_':
                j += 1
            
            # If one pointer reaches the end of its string while the other does not, break
            if i == n or j == n:
                break
            
            # If the characters at the pointers do not match, transformation is impossible
            if start[i] != target[j]:
                return False
            
            # If 'L' is in start and needs to move right (i < j), return False
            if start[i] == 'L' and i < j:
                return False
            
            # If 'R' is in start and needs to move left (i > j), return False
            if start[i] == 'R' and i > j:
                return False
            
            # Move both pointers to the next character
            i += 1
            j += 1
        
        # Both pointers should reach the end of their respective strings
        return i == n and j == n

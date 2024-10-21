class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def backtrack(start: int, unique_substrings: set) -> int:
            # If we reach the end of the string, return the size of unique substrings
            if start == len(s):
                return len(unique_substrings)
            
            max_count = 0  # Variable to keep track of the maximum unique substrings count
            # Iterate over possible end indices for substrings starting from 'start'
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]  # Extract the substring from start to end
                # Check if the substring is unique (not already in the set)
                if substring not in unique_substrings:
                    unique_substrings.add(substring)  # Add the substring to the set
                    # Recursively call backtrack for the next part of the string
                    max_count = max(max_count, backtrack(end, unique_substrings))
                    unique_substrings.remove(substring)  # Backtrack: remove the substring from the set
            return max_count  # Return the maximum count found
        
        # Start the backtracking process from index 0 with an empty set of unique substrings
        return backtrack(0, set())

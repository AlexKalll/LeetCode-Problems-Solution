from typing import List

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        groups = []
        n = len(s)
        
        # Iterate through the string in chunks of size k
        for i in range(0, n, k):
            # Get the current group
            group = s[i:i+k]
            # If the group is less than k, we need to fill it
            if len(group) < k:
                group += fill * (k - len(group))
            groups.append(group)
        
        return groups

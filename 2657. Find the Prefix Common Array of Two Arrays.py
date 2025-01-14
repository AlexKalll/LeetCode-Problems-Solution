# https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/description/

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        C = [0] * n  # Initialize the result list with zeros
        common_count = 0  # To keep track of common elements
        
        # Use sets to track seen elements
        seen_A = set()
        seen_B = set()
        
        for i in range(n):
            # Add current elements to the respective sets
            seen_A.add(A[i])
            seen_B.add(B[i])
            
            # Count common elements by taking the intersection of the sets
            common_count = len(seen_A.intersection(seen_B))
            
            # Store the count in the result array
            C[i] = common_count
        
        return C

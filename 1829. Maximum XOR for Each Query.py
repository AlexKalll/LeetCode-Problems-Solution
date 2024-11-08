class Solution:
    def getMaximumXor(self, array: List[int], bitLimit: int) -> List[int]:
        # Determine the maximum possible value based on the number of bits
        maxPossibleValue = (1 << bitLimit) - 1  # Equivalent to 2^bitLimit - 1
        
        # Calculate the cumulative XOR of all elements in the array
        totalXor = 0
        for value in array:
            totalXor ^= value
        
        # Initialize the result list to store the answers for each element
        xorResults = []
        
        # Process each element in reverse order
        for value in reversed(array):
            # Calculate the result for the current element
            xorResults.append(totalXor ^ maxPossibleValue)
            
            # Update totalXor by removing the effect of the current element
            totalXor ^= value
        
        return xorResults

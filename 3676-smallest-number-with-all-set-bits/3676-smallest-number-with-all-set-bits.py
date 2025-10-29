class Solution:
    def smallestNumber(self, n: int) -> int:
        # Find the position of the most significant bit
        # bit_length() returns the number of bits needed to represent n
        msb = n.bit_length() - 1
        
        # Create a number with (msb+1) bits all set to 1
        result = (1 << (msb + 1)) - 1
        
        return result
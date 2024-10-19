class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # Calculate the length of S_n
        length = (1 << n) - 1  # This is 2^n - 1
        
        # Base case
        if n == 1:
            return "0"
        
        # Find the middle index
        mid = (length + 1) // 2
        
        if k < mid:  # If k is in the first half
            return self.findKthBit(n - 1, k)
        elif k == mid:  # If k is the middle bit
            return "1"
        else:  # If k is in the second half
            # Adjust k to the corresponding position in the inverted and reversed part
            new_k = length - k + 1
            # Invert the bit found in S_{n-1}
            return '0' if self.findKthBit(n - 1, new_k) == '1' else '1'
            
# Time Complexity: O(logn) due to the halving nature of the recursive calls.
# Space Complexity: O(logn) due to the recursive call stack.

"""
Approach
Determine the maximum bit length of the largest number in the list. This will help us know how many bit positions we need to check.
For each bit position, count how many numbers have that specific bit set to 1.
Keep track of the maximum count across all bit positions, which represents the largest combination of numbers that can be formed.
Return this maximum count as the result.
Complexity
Time complexity:O(n⋅k), where ( n ) is the number of candidates and ( k ) is the number of bits in the largest number (up to 32 for typical integers).
Space complexity:O(1), as we are using a constant amount of extra space regardless of the input size
Code """


class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        ans = 0 
        max_bit_len = max(candidates).bit_length() # len of bits of the largest number
        for i in range(max_bit_len):
            temp = sum((c >> i) & 1 for c in candidates) # Count how many numbers have the i-th bit set i.e. 1
            """
            # this is just for testing to show  how it works 
            print(f'i : {i}')
            for c in candidates:
                print(bin(c))
                print(c >> i)
                print(bin(c >> i))
                print((c >> i) & 1)
            print(temp)"""

            ans = max(ans, temp)
        return ans 

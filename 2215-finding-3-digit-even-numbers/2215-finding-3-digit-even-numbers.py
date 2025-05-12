class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        unique_numbers = set()
        even_digits = [d for d in digits if d % 2 == 0]  # Only even digits for the last position
        
        # Generate permutations of length 3
        for perm in permutations(digits, 3):
            # Check if the first digit is not zero and the last digit is even
            if perm[0] != 0 and perm[2] % 2 == 0:
                number = perm[0] * 100 + perm[1] * 10 + perm[2]  # Form the number
                unique_numbers.add(number)
        
        return sorted(unique_numbers)
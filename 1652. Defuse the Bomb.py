class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        # If k is negative, reverse the code and call decrypt with positive k
        if k < 0:
            return self.decrypt(code[::-1], -k)[::-1]
        
        n = len(code)  
        ret = [0] * n  
        s = sum(code[:k])  # Calculate the initial sum of the first k elements
        
        # Debug prints to show initial values
        print("Initial segment:", code[:k])  # Print the first k elements
        print("Initial sum:", s)  # Print the initial sum
        
        # Iterate through each index and value in the code list
        for i, c in enumerate(code):
            # Update the sum by adding the next element and subtracting the current one
            s += code[(i + k) % n] - c
            # Store the updated sum in the result list
            ret[i] = s
            
        return ret

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        # Count the frequency of each number in the array
        ht = Counter(arr)
        
        # Initialize a variable to keep track of the largest lucky integer
        largest_lucky = -1
        
        for num in ht:
            # Check if the number is a lucky integer
            if num == ht[num]:
                # Update the largest lucky integer if this one is larger
                largest_lucky = max(largest_lucky, num)
        
        return largest_lucky
class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        # Create a set of banned numbers
        banned_set = set(banned)
        
        # Initialize the count of chosen numbers
        count = 0
        
        # Initialize the current sum
        current_sum = 0
        
        # Iterate through the range [1, n]
        for i in range(1, n+1):
            # If the current number is not in the banned set
            if i not in banned_set:
                # If adding the current number to the current sum doesn't exceed maxSum
                if current_sum + i <= maxSum:
                    # Increment the count and add the current number to the current sum
                    count += 1
                    current_sum += i
                # If adding the current number to the current sum exceeds maxSum
                else:
                    # Break the loop since we can't add any more numbers
                    break
        
        return count

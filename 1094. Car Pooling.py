class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # Use a lambda function to find the maximum drop-off location
        max_location = max(trips, key=lambda trip: trip[2])[2]  # Extract the maximum drop-off location
        
        # Initialize the prefix sum array with zeros
        prefixSum = [0] * (max_location + 1)

        # Populate the prefix sum array
        for numPassengers, from_i, to_i in trips:
            prefixSum[from_i] += numPassengers  # Pick up passengers
            prefixSum[to_i] -= numPassengers    # Drop off passengers

        # Check if at any point the number of passengers exceeds capacity
        current_passengers = 0
        for passengers in prefixSum:
            current_passengers += passengers
            if current_passengers > capacity:
                return False

        return True

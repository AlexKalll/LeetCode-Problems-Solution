class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        # Create a list of tuples containing arrival time, leaving time, and original index
        times = [(a, l, i) for i, (a, l) in enumerate(times)]
        print(times)  # Debug: print the list of times with indices
        
        # Sort the list of tuples by arrival time
        times.sort()  
        print(times)  # Debug: print the sorted list of times
        
        n = len(times)  # Get the number of friends
        
        # Initialize a list of free chairs as indices from 0 to n-1
        freechairs = list(range(n))  # [index]
        heapify(freechairs)  # Turn the list into a heap for efficient chair allocation
        print(freechairs)  # Debug: print the initial free chairs
        
        usedchairs = []  # List to keep track of used chairs with their leaving times and indices

        # Iterate over each friend's arrival and leaving times
        for a, l, i in times:
            # Free up chairs for friends who have left before the current friend's arrival
            while usedchairs and usedchairs[0][0] <= a:  # Check if the next friend is leaving
                _, idx = heappop(usedchairs)  # Pop the chair of the friend who is leaving
                heappush(freechairs, idx)  # Add the freed chair back to the available chairs
            
            # Allocate the next available chair
            cur = heappop(freechairs)  # Get the index of the next free chair
            
            # If the current friend is the target friend, return the chair index
            if i == targetFriend:
                return cur
            
            # Mark the current chair as used with the friend's leaving time
            heappush(usedchairs, (l, cur))  # Store leaving time and chair index

import heapq
#use a greedy approach with a priority queue (min-heap)
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        # Sort intervals by their start time, and by end time in case of ties(if starting pts match)
        intervals.sort(key=lambda x: (x[0], x[1]))
        
        # Min-heap to track the end times of groups
        heap = []
        
        for interval in intervals:
            # If the heap is not empty and the current interval starts after the
            # earliest ending interval, we can merge it into that group
            if heap and interval[0] > heap[0]:
                heapq.heappop(heap)
            
            # Add the end time of the current interval to the heap
            heapq.heappush(heap, interval[1])
        
        # The size of the heap is the number of groups needed
        return len(heap)

"""
from heapq import heapify

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        # Sort intervals by their start time, and by end time in case of ties
        intervals.sort(key=lambda x: (x[0], x[1]))
        
        # List to track the end times of groups
        end_times = []
        
        for interval in intervals:
            # If there are end times and the current interval starts after the
            # earliest ending interval, we can merge it into that group
            if end_times and interval[0] > end_times[0]:
                end_times.pop(0)  # Remove the earliest end time
            
            # Add the end time of the current interval to the list
            end_times.append(interval[1])
            heapify(end_times)  # Maintain the heap property
        
        # The length of the end_times list is the number of groups needed
        return len(end_times)
    """

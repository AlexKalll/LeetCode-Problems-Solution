class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        min_heap = []

        for i in range(len(heights) - 1):
            height_diff = heights[i + 1] - heights[i]
            if height_diff > 0:
                heapq.heappush(min_heap, height_diff)
            if len(min_heap) > ladders:
                bricks -= heapq.heappop(min_heap)
            if bricks < 0:
                return i
                
        return len(heights) - 1
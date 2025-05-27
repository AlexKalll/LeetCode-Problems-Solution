class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        ops = 0
        while nums[0] < k:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            new_elem = min(x, y) * 2 + max(x, y)
            heapq.heappush(nums, new_elem)
            ops += 1
        return ops
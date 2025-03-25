class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                start = end = mid

                while start - 1 >= 0 and nums[start-1] == target:
                    start -= 1
                
                while end + 1 < len(nums) and nums[end + 1] == target:
                    end += 1

                return [start, end]

        return [-1, -1]


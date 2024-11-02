class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def leftextreme(nums, target, l, r):
            mid = (l + r) // 2

            if nums[mid] == target:
                if mid == 0 or nums[mid - 1] != target:
                    return mid
                else:
                    return leftextreme(nums, target, l, mid - 1)
            if target > nums[mid]:
                return leftextreme(nums, target, mid + 1, r)
            
        def rightextreme(nums, target, l, r):
            mid = (l + r) // 2

            if nums[mid] == target:
                if mid == len(nums) - 1 or nums[mid + 1] != target:
                    return mid
                else:
                    return rightextreme(nums, target, mid + 1, r)

            return rightextreme(nums, target, l, mid - 1)

        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] == target:
                left_index = leftextreme(nums, target, l, mid)
                right_index = rightextreme(nums, target, mid, r)
                return [left_index, right_index]

            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
                
        return [-1, -1]
      
